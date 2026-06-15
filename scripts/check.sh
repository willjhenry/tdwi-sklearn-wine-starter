#!/usr/bin/env bash
# Deterministic pre-commit / pre-push checks (Recipe 1).
# Run from repo root: bash scripts/check.sh

set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> pip install --dry-run"
pip install --dry-run -r requirements.txt

# Optional extension points (uncomment as you adopt):
# echo "==> ruff check"
# ruff check .

echo "==> pytest"
python -m pytest test_model.py
