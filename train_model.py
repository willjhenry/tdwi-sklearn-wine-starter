"""Train a wine cultivar classifier on the sklearn Wine dataset."""

from pathlib import Path

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

MODEL_PATH = Path("models/wine_classifier.joblib")


def load_data():
    data = load_wine()
    return data.data, data.target


def train_and_save_model(X, y, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state
    )
    model = RandomForestClassifier(random_state=random_state)
    model.fit(X_train, y_train)
    return model, X_test, y_test


def main():
    X, y = load_data()
    model, X_test, y_test = train_and_save_model(X, y)
    score = model.score(X_test, y_test)
    print(f"Test accuracy: {score:.3f}")


if __name__ == "__main__":
    main()
