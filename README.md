<div align="left">

# Shoryakumar Mishra

`AI/ML Research · LLM Systems · Computer Vision`

</div>

---

Building at the intersection of large language models, retrieval-augmented generation, and efficient inference — with peer-reviewed work on LLM semantic alignment and production systems deployed at scale.

Apple Swift Student Challenge 2026 Global Winner (~350 / 50,000+). Currently at SRM Institute of Science and Technology (B.Tech CSE, 2027).

---

## Research & Publications

**DriftShield: Clinical Concept Drift & Multimodal RAG Pipeline** — *Peer-Reviewed Preprint*
`Python · PyTorch · HuggingFace · BioBERT · FAISS · FastAPI`

Published research on LLM semantic alignment in clinical settings. Designed a full RAG pipeline — section-aware chunking, BioBERT embeddings, FAISS vector indexing — to intercept temporal guideline drift in downstream clinical LLMs. Developed a safety-first max-ensemble (BioBERT + Qwen CoT) and a cross-attention multimodal CLIP fusion head. Achieved **97.8% sensitivity** and **88.5% specificity** on the ConflictMedQA-Extended benchmark. Automated MLOps telemetry using Kolmogorov-Smirnov tests and Population Stability Index for live distribution drift tracking via Weights & Biases.

---

**Self-Pruning Neural Network with Learned Sparsity**
`Python · PyTorch · NumPy · CUDA`

Designed a PrunableLinear layer with learnable sigmoid gates and L1 sparsity regularisation. Achieved **91.3% weight sparsity** (3.47M of 3.8M parameters pruned) with only **2.6% accuracy loss** on CIFAR-10 — yielding **11.5x parameter compression**. Validated through systematic ablation studies with fully reproducible training scripts. Direct applicability to on-device LLM inference and edge deployment.

---

## Selected Work

**GoblinGuard AI — Real-Time LLM Output Auditor**
`Python · PyTorch · Transformers · Sentence-BERT · Streamlit`

RLHF reward-hacking detector inspired by OpenAI's GPT-5.5 "Goblin Incident". Fuses three ML detectors into a TicScore (0–100): n-gram scanner (lexical spikes), TicAutoencoder (embedding drift via reconstruction error), and a fine-tuned TicClassifier. Inputs embedded with Sentence-BERT (all-MiniLM-L6-v2, 384-dim). Detects reward-hacking artifacts that propagate silently through SFT data reuse into downstream models — critical for safety in medical AI and autonomous systems.

**EvaGuardian — Real-Time Object Detection System**
`Python · PyTorch · YOLOv8 · CUDA · OpenCV · FastAPI`

Trained custom YOLOv8 model on 2,500+ annotated images with CUDA-accelerated GPU training. Achieved **94% mAP@0.5 at 28 FPS** with modular inference pipeline, data augmentation (mosaic, mixup, HSV jitter), and structured FastAPI backend for real-world deployment.

**OncoVision — Lung Cancer Detection CNN**
`TensorFlow · Keras · ResNet-50 · OpenCV · Transfer Learning`

Deep learning CNN achieving **90% accuracy** on histopathological CT scans via fine-tuned ResNet-50 transfer learning. Reduced training time by 35% through augmentation pipelines and class-imbalance correction — solving real-world large-scale medical imaging problems.

---

## Experience

**AI/ML Engineer Intern** · Infosys Springboard · Sep 2024 – Mar 2025

Trained and deployed PyTorch models with Optuna/GridSearchCV hyperparameter optimisation and k-fold cross-validation; improved F1 by 12%. Built end-to-end automated data pipelines covering ingestion, feature engineering, training, and evaluation — reducing manual processing by 40%. Applied probability, statistics, and linear algebra to feature selection (PCA, mutual information), model diagnostics (bias-variance tradeoff, learning curves), and evaluation (precision, recall, AUC-ROC) on class-imbalanced datasets.

**Software Engineer Intern, iOS & Systems** · Infosys × Apple · Apr 2025 – May 2026

Selected in the top 4% (100 of 3,000+ applicants) for Apple's partnered engineering programme. Apple Swift Student Challenge 2026 Global Winner — built AXIS, a real-time sensor-driven app using CoreMotion API. Architected Rentiwise (live on App Store) with REST API pipeline, async/await networking, and in-memory caching — reducing data-fetch latency by 35% while sustaining 60fps UI performance.

**iOS Developer Intern** · Infosys (Fleet Management) · Feb 2026 – Mar 2026

Shipped Fleet Management System with real-time vehicle tracking, driver-assignment workflows, and live dashboards. Ranked **#1 company-wide** across all intern submissions. Delivered 3 production-ready features in 48 hours with zero post-release defects.

---

## Technical Profile

| Domain | Stack |
|---|---|
| ML / DL | PyTorch, TensorFlow, Keras, scikit-learn, XGBoost, LightGBM, CUDA, SHAP, Optuna, W&B |
| NLP / LLM | HuggingFace Transformers, LangChain, OpenAI API, LoRA/QLoRA, RLHF, spaCy |
| CV & RAG | YOLOv8, OpenCV, FAISS, ChromaDB, Semantic Chunking, BERTScore, Vector Indexing |
| Languages | Python (primary), C/C++, Java, SQL, Swift, JavaScript, Go, Bash, R |
| Cloud & Tools | AWS (EC2, S3, SageMaker), Docker, Firebase, FastAPI, Git, CI/CD, Linux |

---

## Certifications & Recognition

- **Apple Swift Student Challenge 2026** — Global Winner (~350 / 50,000+ worldwide)
- **AWS Certified AI Practitioner** · **AWS Certified ML Engineer – Associate**
- **SAP Certified Generative AI Developer** · **NVIDIA: Fundamentals of Deep Learning**
- **Oracle Certified Professional — Generative AI** · **Salesforce Agentforce Specialist (AI)**
- **Guidewire Hackathon** — Top 6 / 5,000+ teams · **Google Code Clash 2.0** — Top 13 / 1,300+ teams
- **Smart India Hackathon 2024** — National Participant (Gov. of India)

---

## Community

- **AI Research Communicator (X/Twitter):** Authored 200+ technical breakdowns of NLP/ML papers — LLMs, Computer Vision, Mechanistic Interpretability, RL — tracking frontier AI research.
- **Associate Head, Content, Placfv's:** Led placement communications for 50+ enterprise recruiters.
- **Committee Head, Aaruush (SRM):** Managed logistics and cross-team coordination for one of India's largest national-level tech festivals.

---

<p align="center">
<a href="mailto:shoryamishra65@gmail.com">Email</a> · <a href="https://linkedin.com/in/shoryakumar-mishra">LinkedIn</a> · <a href="https://twitter.com/smishra61">X / Twitter</a> · <a href="https://github.com/Shoryamishra61">GitHub</a> · <a href="https://leetcode.com/mishrashorya">LeetCode</a> · <a href="https://codeforces.com/profile/mishrashorya61">Codeforces</a>
</p>
