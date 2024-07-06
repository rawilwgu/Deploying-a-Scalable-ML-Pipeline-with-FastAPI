import pytest
import pandas as pd
from ml.model import train_model, compute_model_metrics
from ml.data import process_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def test_model_instance():
    '''
    Tests to confirm that the model is an instance of the given model class.
    '''
    X_dummy = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': ['A', 'B', 'C']})
    y_dummy = pd.Series([0, 1, 0])

    X_dummy_encoded = pd.get_dummies(X_dummy)

    model = train_model(X_dummy_encoded, y_dummy)

    assert isinstance(model, RandomForestClassifier)


def test_metrics():
    """
    Tests to confirm that the computing_model_metrics function works correctly with expected values.
    """
    y_true = pd.Series([0, 1, 0, 1])
    y_pred = pd.Series([0, 0, 1, 1])
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    assert precision == 0.5
    assert recall == 0.5
    assert f1 == 0.5


def test_train_dataset():
    """
    Tests to confirm that the dataset shapes are the correct format.
    """

    data = pd.DataFrame({'feature_1': [1, 2, 3],
                        'feature_2': ['A', 'B', 'C'],
                        'label': [0, 1, 0]
                         }
                        )

    train_data, test_data = train_test_split(data, test_size=0.2)

    assert len(train_data) > 0
    assert len(test_data) > 0
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
