import joblib
import pytest
from sklearn.datasets import load_wine

from train_model import MODEL_PATH, load_data, train_and_save_model


@pytest.fixture
def wine_data():
    return load_data()


def test_load_data_shape(wine_data):
    X, y = wine_data
    assert X.shape[1] == 13, "Wine dataset should have 13 features"
    assert len(y) == 178, "Wine dataset should have 178 samples"


def test_three_classes(wine_data):
    _, y = wine_data
    assert len(set(y)) == 3, "Wine dataset should have 3 cultivar classes"


def test_model_artifact_saved():
    X, y = load_data()
    train_and_save_model(X, y)
    assert MODEL_PATH.exists(), "Trained model must be saved to models/wine_classifier.joblib"


def test_saved_model_predicts_three_classes():
    X, y = load_data()
    train_and_save_model(X, y)
    model = joblib.load(MODEL_PATH)
    predictions = model.predict(X[:5])
    assert all(0 <= label <= 2 for label in predictions), (
        "Predictions should be valid wine class labels (0–2)"
    )


def test_model_accuracy_threshold():
    X, y = load_data()
    model, X_test, y_test = train_and_save_model(X, y)
    score = model.score(X_test, y_test)
    assert score >= 0.85, f"Test accuracy should be at least 0.85 (got {score:.3f})"
