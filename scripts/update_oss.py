from __future__ import annotations

import json
import os
import subprocess
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path


USERNAME = os.getenv("OSS_GITHUB_USER", "Shoryamishra61")

TOKEN = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
if not TOKEN:
    try:
        TOKEN = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    except Exception:
        pass

README = (
    Path(__file__).resolve().parent.parent / "README.md"
    if (Path(__file__).resolve().parent.parent / "README.md").exists()
    else Path("README.md")
)

START = "<!-- OSS-AUTO:START -->"
END = "<!-- OSS-AUTO:END -->"

# Recruiter-facing defaults.
EXCLUDE_OWN_REPOSITORIES = True
INCLUDE_CLOSED_UNMERGED = False
MAX_HIGHLIGHTS_PER_REPO = 2

GRAPHQL_URL = "https://api.github.com/graphql"


QUERY = """
query($query: String!, $cursor: String) {
  search(
    query: $query
    type: ISSUE
    first: 100
    after: $cursor
  ) {
    pageInfo {
      hasNextPage
      endCursor
    }

    nodes {
      ... on PullRequest {
        number
        title
        url
        state
        mergedAt
        createdAt
        updatedAt
        isDraft

        commits {
          totalCount
        }

        closingIssuesReferences(first: 100) {
          totalCount
        }

        repository {
          nameWithOwner
          url
          stargazerCount

          owner {
            login
          }
        }
      }
    }
  }
}
"""


def graphql(query: str, variables: dict) -> dict:
    if not TOKEN:
        raise RuntimeError("GH_TOKEN/GITHUB_TOKEN is not configured and gh auth token unavailable")

    payload = json.dumps({
        "query": query,
        "variables": variables,
    }).encode()

    request = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": f"{USERNAME}-oss-readme",
        },
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read())

    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"], indent=2))

    return data["data"]


def fetch_pull_requests() -> list[dict]:
    prs: list[dict] = []
    cursor = None

    while True:
        data = graphql(
            QUERY,
            {
                "query": f"author:{USERNAME} is:pr",
                "cursor": cursor,
            },
        )

        search = data["search"]

        for node in search["nodes"]:
            if not node or not isinstance(node, dict) or "repository" not in node or not node.get("repository"):
                continue

            repo = node["repository"]

            if (
                EXCLUDE_OWN_REPOSITORIES
                and repo.get("owner", {}).get("login", "").lower() == USERNAME.lower()
            ):
                continue

            merged = node.get("mergedAt") is not None
            opened = node.get("state") == "OPEN"

            # Keep high-signal work only:
            # accepted contributions and currently active PRs.
            if not INCLUDE_CLOSED_UNMERGED and not (merged or opened):
                continue

            prs.append(node)

        if not search["pageInfo"]["hasNextPage"]:
            break

        cursor = search["pageInfo"]["endCursor"]

    return prs


def short_number(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}k"
    return str(value)


def clean_title(title: str, limit: int = 72) -> str:
    title = " ".join(title.split())
    title = title.replace("|", "\\|")

    if len(title) <= limit:
        return title

    return title[: limit - 1].rstrip() + "…"


def badge(label: str, value: int, color: str) -> str:
    label_path = urllib.parse.quote(label, safe="")
    value_path = urllib.parse.quote(str(value), safe="")

    return (
        f"![{label}]"
        f"(https://img.shields.io/badge/"
        f"{label_path}-{value_path}-{color}"
        f"?style=flat-square&logo=github)"
    )


def build_section(prs: list[dict]) -> str:
    grouped: dict[str, dict] = {}

    for pr in prs:
        repo = pr["repository"]
        name = repo["nameWithOwner"]

        if name not in grouped:
            grouped[name] = {
                "name": name,
                "url": repo["url"],
                "stars": repo.get("stargazerCount", 0),
                "prs": [],
            }

        grouped[name]["prs"].append(pr)

    repositories = sorted(
        grouped.values(),
        key=lambda item: (-item["stars"], item["name"].lower()),
    )

    total_prs = len(prs)
    merged_prs = sum(1 for pr in prs if pr.get("mergedAt"))
    open_prs = sum(1 for pr in prs if pr.get("state") == "OPEN")

    # Commits contained in the OSS pull requests represented here.
    total_pr_commits = sum(
        (pr.get("commits") or {}).get("totalCount", 0)
        for pr in prs
    )

    # Only issues that GitHub explicitly associates with accepted,
    # merged pull requests are counted as "solved".
    total_issues_solved = sum(
        (pr.get("closingIssuesReferences") or {}).get("totalCount", 0)
        for pr in prs
        if pr.get("mergedAt")
    )

    lines = [
        START,
        "",
        (
            f"{badge('Pull Requests', total_prs, '0969da')} "
            f"{badge('Merged PRs', merged_prs, '2ea44f')} "
            f"{badge('Open PRs', open_prs, 'd29922')} "
            f"{badge('Issues Solved', total_issues_solved, '8250df')} "
            f"{badge('PR Commits', total_pr_commits, '6e7781')}"
        ),
        "",
        (
            "> Public upstream contributions · automatically updated · "
            "repositories ranked by current GitHub stars"
        ),
        "",
        (
            "| Repository | Stars | PRs | Merged | Open | "
            "PR Commits | Issues Solved | What I changed |"
        ),
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]

    for repo in repositories:
        repo_prs = repo["prs"]

        merged = [pr for pr in repo_prs if pr.get("mergedAt")]
        opened = [pr for pr in repo_prs if pr.get("state") == "OPEN"]

        commit_count = sum(
            (pr.get("commits") or {}).get("totalCount", 0)
            for pr in repo_prs
        )

        issues_solved = sum(
            (pr.get("closingIssuesReferences") or {}).get("totalCount", 0)
            for pr in merged
        )

        # Merged work first, then open work.
        ordered = sorted(
            repo_prs,
            key=lambda pr: (
                pr.get("mergedAt") is None,
                pr.get("updatedAt", ""),
            ),
            reverse=False,
        )

        highlights = []

        for pr in ordered[:MAX_HIGHLIGHTS_PER_REPO]:
            status = "✅" if pr.get("mergedAt") else "🟡"
            title = clean_title(pr.get("title", ""))

            highlights.append(
                f'{status} [#{pr["number"]}]({pr["url"]}) — {title}'
            )

        summary = "<br>".join(highlights)

        lines.append(
            f'| [{repo["name"]}]({repo["url"]}) '
            f'| ⭐ {short_number(repo["stars"])} '
            f'| {len(repo_prs)} '
            f'| {len(merged)} '
            f'| {len(opened)} '
            f'| {commit_count} '
            f'| {issues_solved} '
            f'| {summary} |'
        )

    encoded_user = urllib.parse.quote(USERNAME, safe="")

    lines += [
        "",
        (
            f"[View all pull requests]"
            f"(https://github.com/pulls?"
            f"q=is%3Apr+author%3A{encoded_user})"
            " · "
            f"[Merged pull requests]"
            f"(https://github.com/pulls?"
            f"q=is%3Apr+is%3Amerged+author%3A{encoded_user})"
        ),
        "",
        "<sub>Generated from the GitHub API. ⭐ counts update automatically.</sub>",
        "",
        END,
    ]

    return "\n".join(lines)


def update_readme(section: str) -> None:
    text = README.read_text(encoding="utf-8")

    if START not in text or END not in text:
        raise RuntimeError(
            f"README must contain both {START!r} and {END!r}"
        )

    before = text.split(START, 1)[0]
    after = text.split(END, 1)[1]

    updated = before.rstrip() + "\n\n" + section + after

    README.write_text(updated, encoding="utf-8")


def main() -> None:
    prs = fetch_pull_requests()

    if not prs:
        raise RuntimeError(
            f"No qualifying OSS pull requests found for {USERNAME}"
        )

    section = build_section(prs)
    update_readme(section)

    print(
        f"Updated README: "
        f"{len(prs)} qualifying PRs across "
        f"{len({pr['repository']['nameWithOwner'] for pr in prs})} repositories"
    )


if __name__ == "__main__":
    main()
