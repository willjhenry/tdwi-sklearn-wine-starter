"""Reference acceptance tests — instructor / main-working-example only.

Copy to repo-root test_model.py on a working branch. Filename avoids pytest auto-discovery.
"""

import joblib
import pytest

from train_model import MODEL_PATH, train_and_save_model
from wine_data import get_train_test_split, load_features_and_target


@pytest.fixture
def wine_data():
    return load_features_and_target()


def test_load_data_shape(wine_data):
    X, y = wine_data
    assert X.shape[1] == 13, "Wine dataset should have 13 features"
    assert len(y) == 178, "Wine dataset should have 178 samples"


def test_three_classes(wine_data):
    _, y = wine_data
    assert len(set(y)) == 3, "Wine dataset should have 3 cultivar classes"


def test_model_artifact_saved():
    X_train, X_test, y_train, y_test = get_train_test_split()
    train_and_save_model(X_train, X_test, y_train, y_test)
    assert MODEL_PATH.exists(), (
        "Trained model must be saved to models/wine_classifier.joblib"
    )


def test_saved_model_predicts_three_classes():
    X_train, X_test, y_train, y_test = get_train_test_split()
    train_and_save_model(X_train, X_test, y_train, y_test)
    model = joblib.load(MODEL_PATH)
    X, _ = load_features_and_target()
    predictions = model.predict(X[:5])
    assert all(0 <= label <= 2 for label in predictions), (
        "Predictions should be valid wine class labels (0–2)"
    )


def test_model_accuracy_threshold():
    X_train, X_test, y_train, y_test = get_train_test_split()
    model, X_test, y_test = train_and_save_model(
        X_train, X_test, y_train, y_test
    )
    score = model.score(X_test, y_test)
    assert score >= 0.95, (
        f"Holdout accuracy should be at least 0.95 (got {score:.3f})"
    )
