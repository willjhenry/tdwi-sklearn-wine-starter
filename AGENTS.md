# AGENTS.md

## Overview

This is a Python machine-learning starter repo for the TDWI "Agentic Code Generation" lab (Lab 2). Students build a **scikit-learn** Wine cultivar classifier from a spec (`SPEC.md`), add acceptance tests during the lab, and save a model artifact.

This is a **hands-on workshop** repository, not production code. The **user's prompt** defines the task for each agent session. Do not reorganize the repo or change import paths unless the user asks.

### Human-only lab docs

These files are for **humans** during the workshop. They exist in the repo but are **not** your runbook:

- **`README.md`** — one-time setup (GitHub, fork, clone, local `.venv`, test push). **Do not** follow or repeat these steps.
- **`LAB2-Local-Agent-Wine-Classifier.ipynb`** — lab walkthrough (local agent, `check.sh`, `/commit-code`). **Do not** follow notebook steps unless the user asks you to implement a specific lab step.

Use **this file (`AGENTS.md`)**, the user's prompt, and the Python source as your source of truth. Do not modify the lab notebook unless the user explicitly asks.

### Repo layout

Starter files live at the repo root:

- `wine_data.py` — Wine dataset load + fixed train/test split (provided)
- `SPEC.md` — project spec template (not `requirements.txt`); students fill this in during the lab (follow the user's version when implementing)
- `train_model.py` — training code (incomplete in the starter; implement per `SPEC.md`)

There is **no** `test_model.py` on the starter fork—create it per `SPEC.md` when the user asks.

Model artifacts:

- `models/wine_classifier.joblib` — saved classifier (created by `train_model.py`)

Reference examples (do not copy verbatim unless the user asks): `examples/specs/`, `examples/reference/`.

## Core workflow rules

### Training

```bash
python train_model.py
```

### Running tests

Once `test_model.py` exists:

```bash
python -m pytest
```

When implementing per `SPEC.md`:

- Write or update **acceptance tests** in `test_model.py` from the spec's success metrics **before** implementing training code—not as an afterthought.
- Run `python -m pytest` after changes; fix failures before claiming the task is done.
- Keep tests passing as you extend or refactor the model.

### Before committing

Run the deterministic check script and fix all failures. Re-run until exit code 0:

```bash
bash scripts/check.sh
```

If the user has created **`.cursor/commands/commit-code.md`**, they may invoke **`/commit-code`**, which runs `check.sh`, optional sub-agent review, then suggests a commit message from staged changes. Do not assume that command exists until the user adds it.
