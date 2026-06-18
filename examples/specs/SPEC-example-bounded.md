# Wine classifier — spec (example: bounded scope)

**Instructor / reference only.** Copy ideas into your own `SPEC.md` during the lab, or use as a fallback if elicitation runs long. Not a student handout path in the notebook—point to `examples/specs/` only if you need a rescue.

## Goal

Build a scikit-learn classifier that predicts **wine cultivar** (3 classes) from the sklearn **Wine** dataset chemical features.

## Success metrics

- **Holdout test accuracy ≥ 0.95** on the fixed test set provided in `wine_data.py`
- Primary metric: **accuracy**

## Modeling approach

- **Algorithm:** `LogisticRegression` inside a `Pipeline` with `StandardScaler`
- **Hyperparameter search:** `GridSearchCV` with **5-fold CV** on the **training** split only
- **Search only** regularization strength `C`: `[0.01, 0.1, 1, 10, 100]`
- Use `random_state=42` where applicable for reproducibility
- Do **not** try other model families or large hyperparameter grids in this lab

## Deliverables

- Implement training in `train_model.py` (use `wine_data.py` for load + split)
- Save the best fitted pipeline to **`models/wine_classifier.joblib`**
- `python train_model.py` prints holdout accuracy
- Agent adds `test_model.py` from success metrics; all acceptance tests pass

## Out of scope

- Deep learning, XGBoost, random forests
- Plots, Streamlit, or REST API
- Changing the train/test split defined in the starter
- New dependencies beyond `requirements.txt`

## Open questions

- (none — resolved before implementation)
