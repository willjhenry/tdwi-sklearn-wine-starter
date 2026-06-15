# AGENTS.md

## Overview

This is a Python machine-learning starter repo for the TDWI "Agentic Code Generation" lab (Lab 2). It trains a **scikit-learn** classifier on the **Wine** dataset, runs tests, and saves a model artifact.

This is a **hands-on workshop** repository, not production code. The **user's prompt** defines the task for each agent session. Do not reorganize the repo or change import paths unless the user asks.

### Human-only lab docs

These files are for **humans** during the workshop. They exist in the repo but are **not** your runbook:

- **`README.md`** — one-time setup (GitHub, fork, clone, local `.venv`, test push). **Do not** follow or repeat these steps.
- **`LAB2-Local-Agent-Wine-Classifier.ipynb`** — lab walkthrough (local agent, `check.sh`, `/commit-code`). **Do not** follow notebook steps unless the user asks you to implement a specific lab step.

Use **this file (`AGENTS.md`)**, the user's prompt, and the Python source/tests as your source of truth. Do not modify the lab notebook unless the user explicitly asks.

### Repo layout

Starter files live at the repo root:

- `train_model.py` — load Wine data, train classifier, save artifact
- `test_model.py` — pytest tests

Model artifacts:

- `models/wine_classifier.joblib` — saved classifier (created by `train_model.py`)

## Core workflow rules

### Training

```bash
python train_model.py
```

### Running tests

```bash
python -m pytest test_model.py
```

### Before committing

Run the deterministic check script and fix all failures. Re-run until exit code 0:

```bash
bash scripts/check.sh
```

For commits, the user may invoke **`/commit-code`** (Cursor slash command), which runs `check.sh`, optional sub-agent review, then suggests a commit message from staged changes.
