"""Load the sklearn Wine dataset and provide a fixed train/test split."""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


def load_features_and_target():
    """Return feature matrix X and target vector y for the Wine dataset."""
    data = load_wine()
    return data.data, data.target


def get_train_test_split(random_state=42, test_size=0.2):
    """Return a fixed holdout split. Do not change unless REQUIREMENTS.md says so."""
    X, y = load_features_and_target()
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
