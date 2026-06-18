# Wine classifier — requirements (example: minimal)

**Instructor / reference only.** Shorter spec for a **~45 min** variant: less elicitation, faster plan/execute. Students should still write their own `REQUIREMENTS.md` in a full-length lab.

## Goal

Train a logistic regression wine cultivar classifier on the provided Wine data.

## Success metrics

- Holdout accuracy ≥ 0.95

## Modeling approach

- `StandardScaler` + `LogisticRegression`
- `GridSearchCV` over `C` = `[0.01, 0.1, 1, 10, 100]`, 5-fold CV on train

## Deliverables

- `train_model.py` saves `models/wine_classifier.joblib`
- Agent adds `test_model.py` from success metrics; all acceptance tests pass

## Out of scope

- Other algorithms, plotting, APIs

## Open questions

- (none)
