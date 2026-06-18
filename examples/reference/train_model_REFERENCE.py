"""Reference training implementation — instructor / main-working-example only.

Copy to repo-root train_model.py on a working branch. Not collected by pytest.
"""

from pathlib import Path

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

MODEL_PATH = Path("models/wine_classifier.joblib")


def train_and_save_model(X_train, X_test, y_train, y_test, random_state=42):
    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, random_state=random_state)),
        ]
    )
    search = GridSearchCV(
        pipeline,
        param_grid={"clf__C": [0.01, 0.1, 1, 10, 100]},
        cv=5,
        scoring="accuracy",
    )
    search.fit(X_train, y_train)
    best_model = search.best_estimator_
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)
    return best_model, X_test, y_test


def main():
    from wine_data import get_train_test_split

    X_train, X_test, y_train, y_test = get_train_test_split()
    model, X_test, y_test = train_and_save_model(
        X_train, X_test, y_train, y_test
    )
    score = model.score(X_test, y_test)
    print(f"Holdout accuracy: {score:.3f}")


if __name__ == "__main__":
    main()
