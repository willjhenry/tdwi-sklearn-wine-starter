# Wine classifier — spec

Fill this in with your agent during the lab. Do not implement until you and the agent agree on the spec.

**Not** [`requirements.txt`](requirements.txt) — that file lists Python packages. This file is your **project spec** (goal, metrics, deliverables).

## Goal

Classify wine **cultivar** (3 classes) from the chemical features in the sklearn **Wine** dataset. Use the loaders and fixed holdout split already provided in `wine_data.py`.

## Success metrics

- Primary metric: **accuracy**
- Holdout accuracy **≥ 0.95** on the test set from `wine_data.get_train_test_split()` (do not redefine the split)
- `python train_model.py` prints that holdout accuracy
- After training, the fitted pipeline exists at `models/wine_classifier.joblib`

## Modeling approach

- **Preprocessing:** `StandardScaler` in a scikit-learn `Pipeline`
- **Estimator:** `LogisticRegression` (`max_iter=1000`, `random_state=42`)
- **Tuning:** `GridSearchCV` over **regularization `C` only**: `[0.01, 0.1, 1, 10, 100]`
- **CV:** 5-fold cross-validation on the **training** split only (`scoring="accuracy"`)
- Fit the search on train; evaluate the best estimator on the provided holdout test set
- Use `random_state=42` where applicable

## Deliverables

- `test_model.py` — acceptance tests derived from **Success metrics** (artifact path, holdout accuracy ≥ 0.95, valid cultivar predictions)
- `train_model.py` — train using `wine_data.py`, run `GridSearchCV`, print holdout accuracy, save the best fitted pipeline
- Saved artifact: **`models/wine_classifier.joblib`**

## Out of scope

- Deep learning, XGBoost, random forests, or other model families
- Large hyperparameter grids beyond `C`
- Plots, Streamlit, dashboards, or a REST API
- Changing the train/test split in `wine_data.py`
- New Python packages beyond `requirements.txt`

## Open questions

- (none — recommended lab scope agreed before implementation)
