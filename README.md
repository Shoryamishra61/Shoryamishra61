"Raise yourself by yourself; do not let yourself fall."

<!-- Apple Swift Student Challenge 2026 · Global Winner -->

# Shoryakumar Mishra


![Apple Swift Student Challenge 2026](https://img.shields.io/badge/Apple_Swift_Student_Challenge_2026-Global_Winner-black?style=for-the-badge&logo=apple)

![AI/ML Research](https://img.shields.io/badge/AI%2FML_Research-black?style=flat-square)
![LLM Systems](https://img.shields.io/badge/LLM_Systems-grey?style=flat-square)
![Computer Vision](https://img.shields.io/badge/Computer_Vision-grey?style=flat-square)

Machine learning engineer focused on LLM alignment, concept drift detection,
and on-device inference. B.Tech CSE · SRMIST Chennai · 2023–2027.

[shoryamishra65@gmail.com](mailto:shoryamishra65@gmail.com) · 
[linkedin](https://linkedin.com/in/shoryakumar-mishra) · 
[X/twitter](https://twitter.com/SMishra61)

---

## Research Interests

Large language model alignment and evaluation · Concept drift detection in clinical NLP pipelines · Efficient neural architectures and learned sparsity · On-device sensor-fusion ML systems · Retrieval-augmented generation

---

## Selected Work

### DriftShield — Semantic Drift Detection in Clinical LLMs
`Python · PyTorch · HuggingFace · BioBERT · FAISS · FastAPI`

Peer-reviewed research on temporal alignment drift in production LLMs (GPT-4, Llama-2, Mistral) exposed to evolving clinical guidelines. The core contribution is a RAG pipeline with section-aware semantic chunking, BioBERT embeddings, and FAISS vector indexing designed to intercept guideline drift before it propagates to downstream inference.

- Evaluation on ConflictMedQA-Extended: 97.8% sensitivity, 88.5% specificity
- 18% reduction in false-positive drift flags via max-ensemble (BioBERT + Qwen CoT)
- Automated MLOps telemetry: KS-tests and Population Stability Index for live distribution monitoring via W&B

---

### GoblinGuardAI — RLHF Reward-Hacking Detector
`Python · PyTorch · Sentence-BERT · Transformers · Streamlit`

An LLM output auditor targeting reward-hacking artifacts that propagate silently through SFT data pipelines. Motivated by OpenAI's documented alignment failures in RLHF training. Three detection signals are fused into a composite TicScore (0–100): n-gram lexical drift scanner, TicAutoencoder reconstruction error over Sentence-BERT embeddings (all-MiniLM-L6-v2, 384-dim), and a fine-tuned TicClassifier. Outputs structured JSON reports. Relevant to safety-critical deployment contexts: medical AI, autonomous decision systems.

---

### Self-Pruning Neural Network with Learned Sparsity
`Python · PyTorch · CIFAR-10 · CUDA`

Novel `PrunableLinear` layer with learnable sigmoid gates and L1 sparsity regularisation. Validated through systematic ablation across sparsity coefficients, gate initialisation schemes, and fine-tuning schedules.

- 91.3% weight sparsity (3.47M of 3.8M parameters pruned)
- 2.6% accuracy degradation on CIFAR-10 at 11.5× compression
- Direct applicability to on-device LLM inference and edge deployment

---

### Eva Guardian — Real-Time Object Detection Pipeline
`Python · PyTorch · YOLOv8 · CUDA · OpenCV · FastAPI`

Custom YOLOv8 model trained on 2,500+ annotated synthetic images (COCO-format, 25 GB) for real-time object recognition in constrained operational environments. Augmentation strategy: mosaic composition, mixup regularisation, HSV-jitter. Modular FastAPI inference backend with confidence-threshold controls.

- mAP@0.5: 0.936 · Precision: 0.967 · Recall: 0.895
- 28 FPS inference on GPU; fault-tolerant training with CUDA OOM recovery

---

### OncoVision — Lung Cancer Classification CNN
`TensorFlow · Keras · ResNet-50 · Transfer Learning · OpenCV`

Transfer learning–based classifier on histopathological CT scans. Fine-tuned ResNet-50 backbone; addressed class imbalance via augmentation pipeline (rotation, elastic distortion, colour jitter). 90% classification accuracy; 35% reduction in training time versus scratch training.

---

## Engineering Experience

**AI / ML Engineer Intern** — Infosys Springboard *(Sep 2024 – Mar 2025, Remote)*  
Trained and deployed PyTorch models with Optuna/GridSearchCV hyperparameter search and k-fold cross-validation; F1 improved 12% on class-imbalanced real-world datasets. Built modular, reproducible data pipelines (ingestion → feature engineering → model training → evaluation), reducing manual preprocessing effort by 40%.

**Software Engineer Intern, iOS & Systems** — Infosys × Apple iOS Dev Centre, SRMIST *(Apr 2025 – May 2026)*  
Selected in the top 4% (100 of 3,000+ applicants). Apple Swift Student Challenge 2026 Global Winner (~350 selected from 50,000+ worldwide): built AXIS, a real-time sensor-fusion application leveraging CoreMotion and HeadphoneMotionManager for on-device posture analytics — fully offline, zero network dependency. Also architected Rentiwise (live on App Store): async/await networking, in-memory caching, REST API pipeline; data-fetch latency reduced 35% at sustained 60 fps.

**iOS Developer Intern** — Infosys Fleet Management Systems, Mysore *(Feb 2026 – Mar 2026)*  
Designed and shipped a Fleet Management System with real-time vehicle tracking, spatial indexing, and graph-based routing. Ranked #1 across all intern submissions company-wide. Delivered 3 production-ready features within a 48-hour sprint; cleared full QA with zero post-release defects.

---

## Technical Skills

| Domain | Tools & Frameworks |
|---|---|
| ML / DL | PyTorch, TensorFlow, Keras, scikit-learn, XGBoost, CUDA, SHAP, Optuna, W&B |
| NLP / LLM | HuggingFace Transformers, LangChain, OpenAI API, LoRA/QLoRA, RLHF, spaCy |
| RAG & Retrieval | FAISS, ChromaDB, BERTScore, semantic chunking, cosine-similarity retrieval |
| CV | YOLOv8, OpenCV, ResNet-50, transfer learning |
| Infrastructure | FastAPI, Docker, AWS (EC2, S3, SageMaker), Firebase, Git, CI/CD, Linux |
| Languages | Python (primary), C/C++, Java, SQL, Swift, Go, Bash |

---

## Recognitions

- **Apple Swift Student Challenge 2026** — Global Winner (~350 of 50,000+ worldwide submissions)
- **Guidewire Hackathon** — Top 6 of 5,000+ teams (GigBuddy: ML-powered parametric insurance risk engine)
- **Google CodeClash 2.0** — Top 13 of 1,300+ teams
- **Smart India Hackathon 2024** — National Participant (Government of India flagship programme)
- **DriftShield** — Peer-reviewed publication in NLP / clinical AI safety

---

## Certifications

AWS Certified AI Practitioner · AWS Certified ML Engineer – Associate · NVIDIA: Fundamentals of Deep Learning · Oracle: Generative AI Professional · SAP Certified GenAI Developer · Salesforce Agentforce Specialist

---

## Open Source Contributions

<!-- OSS-AUTO:START -->

![Pull Requests](https://img.shields.io/badge/Pull%20Requests-19-0969da?style=flat-square&logo=github) ![Merged PRs](https://img.shields.io/badge/Merged%20PRs-11-2ea44f?style=flat-square&logo=github) ![Open PRs](https://img.shields.io/badge/Open%20PRs-8-d29922?style=flat-square&logo=github) ![Issues Solved](https://img.shields.io/badge/Issues%20Solved-3-8250df?style=flat-square&logo=github) ![PR Commits](https://img.shields.io/badge/PR%20Commits-28-6e7781?style=flat-square&logo=github)

> Top 5 upstream contributions · ranked by stars with merged PR weightage · automatically updated

| Repository | Stars | PRs | Merged | Open | PR Commits | Issues Solved | What I changed |
|---|---:|---:|---:|---:|---:|---:|---|
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | ⭐ 103.5k | 1 | 0 | 1 | 1 | 0 | 🟡 [#196873](https://github.com/pytorch/pytorch/pull/196873) — [inductor] Handle full randperm in index_add pattern |
| [apache/hamilton](https://github.com/apache/hamilton) | ⭐ 2.6k | 1 | 1 | 0 | 2 | 1 | ✅ [#1716](https://github.com/apache/hamilton/pull/1716) — fix(caching): avoid storing metadata and results for CachingBehavior.IG… |
| [llvm/llvm-project](https://github.com/llvm/llvm-project) | ⭐ 40.8k | 1 | 0 | 1 | 2 | 0 | 🟡 [#225370](https://github.com/llvm/llvm-project/pull/225370) — [mlir][async] Clamp per-axis trip counts in async-parallel-for |
| [pola-rs/polars](https://github.com/pola-rs/polars) | ⭐ 39.9k | 1 | 0 | 1 | 2 | 0 | 🟡 [#29361](https://github.com/pola-rs/polars/pull/29361) — fix: Preserve timezone offsets when reading JSON datetimes |
| [jax-ml/jax](https://github.com/jax-ml/jax) | ⭐ 36.4k | 1 | 0 | 1 | 1 | 0 | 🟡 [#40821](https://github.com/jax-ml/jax/pull/40821) — jax.scipy.linalg.solve: raise NotImplementedError for assume_a in ('sym… |

[View all pull requests](https://github.com/pulls?q=is%3Apr+author%3AShoryamishra61) · [Merged pull requests](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3AShoryamishra61)

<sub>Generated from the GitHub API. ⭐ counts update automatically.</sub>

<!-- OSS-AUTO:END -->

---

## Writing & Community

Publish technical breakdowns of NLP and ML research papers on [X/Twitter](https://twitter.com/SMishra61) — covering LLMs, mechanistic interpretability, computer vision, and reinforcement learning. 200+ posts; audience is practitioners and researchers.

---

*Open to research collaborations, internships, and full-time roles in ML engineering and applied AI.*

<p align="left">
  <img src="https://komarev.com/ghpvc/?username=ShoryaMishra&label=Profile%20views&color=0e75b6&style=flat" alt="profile views" />
</p>
