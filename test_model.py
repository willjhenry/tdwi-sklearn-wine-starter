"""Acceptance tests for the wine cultivar classifier (from SPEC.md)."""

import joblib
import pytest

from train_model import MODEL_PATH, train_and_save_model
from wine_data import get_train_test_split, load_features_and_target


@pytest.fixture
def holdout_split():
    return get_train_test_split()


def test_trained_model_is_saved_to_specified_path(holdout_split):
    X_train, X_test, y_train, y_test = holdout_split
    train_and_save_model(X_train, X_test, y_train, y_test)
    assert MODEL_PATH.exists(), (
        "Trained model must be saved to models/wine_classifier.joblib"
    )


def test_saved_model_predicts_valid_cultivar_labels(holdout_split):
    X_train, X_test, y_train, y_test = holdout_split
    train_and_save_model(X_train, X_test, y_train, y_test)
    model = joblib.load(MODEL_PATH)
    X, _ = load_features_and_target()
    predictions = model.predict(X[:5])
    assert all(0 <= label <= 2 for label in predictions), (
        "Predictions should be valid wine class labels (0–2)"
    )


def test_holdout_accuracy_meets_spec_threshold(holdout_split):
    X_train, X_test, y_train, y_test = holdout_split
    model, X_test, y_test = train_and_save_model(
        X_train, X_test, y_train, y_test
    )
    score = model.score(X_test, y_test)
    assert score >= 0.95, (
        f"Holdout accuracy should be at least 0.95 (got {score:.3f})"
    )
