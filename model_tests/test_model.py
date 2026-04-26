import sys
from pathlib import Path

import joblib
import numpy as np
import pytest
from sklearn.metrics import accuracy_score

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import load_data, preprocess_data  # noqa: E402


MODEL_PATH = PROJECT_ROOT / "models" / "model.pkl"
TRAIN_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "adult.data"
TEST_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "adult.test"


def test_model_loading():
    assert MODEL_PATH.exists(), f"Model file not found at {MODEL_PATH}"

    try:
        joblib.load(MODEL_PATH)
    except Exception as e:
        pytest.fail(f"Failed to load model: {e}")


def test_prediction_shape():
    model = joblib.load(MODEL_PATH)

    sample_input = np.random.rand(5, model.n_features_in_)
    predictions = model.predict(sample_input)

    assert predictions.shape == (5,), f"Expected predictions of shape (5,), got {predictions.shape}"


def test_prediction_values():
    model = joblib.load(MODEL_PATH)

    sample_input = np.random.rand(5, model.n_features_in_)
    predictions = model.predict(sample_input)

    assert set(predictions).issubset({0, 1}), f"Predictions contain unexpected classes: {set(predictions)}"


def test_model_accuracy():
    model = joblib.load(MODEL_PATH)

    train_df, test_df = load_data(TRAIN_DATA_PATH, TEST_DATA_PATH)
    _, X_test, _, y_test, _, _ = preprocess_data(train_df, test_df)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    assert accuracy >= 0.80, f"Model accuracy below expected threshold: {accuracy:.2f}"