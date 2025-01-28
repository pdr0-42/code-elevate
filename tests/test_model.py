import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.model.model import MlFlowModel

class MockConfig:
    MLFLOW_TRACKING_URI = "http://mock-tracking-uri"
    MODEL = "mock-model-path"

@pytest.fixture
def mock_config():
    return MockConfig()

@pytest.fixture
def test_data():
    return pd.DataFrame({"feature1": [1.0], "feature2": [2.0]})

def test_mlflow_model_initialization(mock_config):
    model = MlFlowModel(mock_config.MODEL)
    assert model.model_path == mock_config.MODEL

@patch("mlflow.pyfunc.load_model")
@patch("mlflow.set_tracking_uri")
def test_load_model(mock_set_tracking_uri, mock_load_model, mock_config):
    mock_model = MagicMock()
    mock_load_model.return_value = mock_model

    model = MlFlowModel(mock_config.MODEL)

    with patch("src.app.config.config.MLFLOW_TRACKING_URI", new=mock_config.MLFLOW_TRACKING_URI):
        loaded_model = model.load_model()

    mock_set_tracking_uri.assert_called_once_with(mock_config.MLFLOW_TRACKING_URI)

    mock_load_model.assert_called_once_with(mock_config.MODEL)
    assert loaded_model == mock_model


@patch("mlflow.pyfunc.load_model")
def test_predict(mock_load_model, mock_config, test_data):
    mock_model = MagicMock()
    mock_model.predict.return_value = ["mock-prediction"]

    mock_load_model.return_value = mock_model

    model = MlFlowModel(mock_config.MODEL)

    prediction = model.predict(test_data)

    mock_load_model.assert_called_once_with(mock_config.MODEL)
    mock_model.predict.assert_called_once_with(test_data)

    assert prediction == "mock-prediction"
