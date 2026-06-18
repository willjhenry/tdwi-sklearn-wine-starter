# Examples (reference)

Lab 2 ships **`scripts/check.sh`** on `main`. **`/commit-code` is not** on starter `main`—students create it in class from the notebook or the copy below.

| Path | Purpose |
|------|---------|
| [`cursor/commands/commit-code.md`](cursor/commands/commit-code.md) | **In-class copy source** for `.cursor/commands/commit-code.md` (Recipe 3) |
| [`specs/SPEC-example-bounded.md`](specs/SPEC-example-bounded.md) | Filled spec (recommended scope)—instructor fallback |
| [`specs/SPEC-example-minimal.md`](specs/SPEC-example-minimal.md) | Shorter filled spec (~45 min variant) |
| [`reference/train_model_REFERENCE.py`](reference/train_model_REFERENCE.py) | Working training script—for `main-working-example` branch only |
| [`reference/model_acceptance_REFERENCE.py`](reference/model_acceptance_REFERENCE.py) | Reference acceptance tests—copy/rename to `test_model.py` on working branch |

Students co-write the real spec in repo-root [`SPEC.md`](../SPEC.md) during the lab (not [`requirements.txt`](../requirements.txt), which lists Python packages).

**Reference files:** not imported by student code. Filenames avoid `test_*.py` / `*_test.py` so `python -m pytest .` does not collect them. Copy to repo root when building an instructor dry-run branch.

For advanced recipes, see [WORKFLOW_RECIPES.md](../WORKFLOW_RECIPES.md).
