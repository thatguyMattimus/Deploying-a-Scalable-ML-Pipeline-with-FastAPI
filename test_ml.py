import pytest
# TODO: add necessary import
from sklearn.linear_model import LogisticRegression
import numpy as np

from ml.model import (
    inference,
    train_model,
)

# TODO: implement the first test. Change the function name and input as needed
def test_model_creation():
    """
    # Tests LogisticRegression creation with random data using train_model function.
    """
    # Your code here
    X_train = np.random.rand(50, 5)
    y_train = np.random.randint(0, 2, size=50)

    model_test = train_model(X_train, y_train)

    assert isinstance(model_test, LogisticRegression)


# TODO: implement the second test. Change the function name and input as needed
def test_model_prediction():
    """
    # Tests Prediction of LogisticRegression with random data using inference function.
    """
    X_train = np.random.rand(50, 5)
    y_train = np.random.randint(0, 2, size=50)
    X_test = np.random.rand(10, 5)

    model_test = train_model(X_train, y_train)
    preds = inference(model_test, X_test)

    assert preds.shape[0] == X_test.shape[0]


# TODO: implement the third test. Change the function name and input as needed
def test_prediction_binary():
    """
    # Tests that the Predictions are valid binary labels before moving forward
    """
    # Your code here
    X_train = np.random.rand(50, 5)
    y_train = np.random.randint(0, 2, size=50)
    X_test = np.random.rand(10, 5)

    model_test = train_model(X_train, y_train)
    preds = inference(model_test, X_test)

    assert all(p in [0,1] for p in preds)
