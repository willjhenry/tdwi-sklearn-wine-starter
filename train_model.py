"""Train a wine cultivar classifier — implement per SPEC.md."""

from pathlib import Path

MODEL_PATH = Path("models/wine_classifier.joblib")


def train_and_save_model(X_train, X_test, y_train, y_test, random_state=42):
    raise NotImplementedError("Implement per SPEC.md")


def main():
    from wine_data import get_train_test_split

    X_train, X_test, y_train, y_test = get_train_test_split()
    train_and_save_model(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
