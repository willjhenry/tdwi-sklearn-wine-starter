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

# Exit code 5 = no tests collected yet (OK before students add test_model.py).
echo "==> pytest"
python -m pytest . || test $? -eq 5
