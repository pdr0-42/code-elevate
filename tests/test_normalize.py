import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.preprocessing.normalize import normalize_data, denormalized_data


class MockRequest:
    def __init__(self, **kwargs):
        self.data = kwargs

    def model_dump(self):
        return self.data


@pytest.fixture
def mock_request():
    return MockRequest(feature1=10.0, feature2=20.0)


@patch("src.preprocessing.normalize.scaler")
def test_normalize_data(mock_scaler, mock_request):
    mock_scaler.transform.return_value = [[0.5, 1.0]]

    normalized_df = normalize_data(mock_request)

    called_data = mock_scaler.transform.call_args[0][0]

    expected_data = pd.DataFrame([mock_request.model_dump()])
    pd.testing.assert_frame_equal(called_data, expected_data)

    expected_df = pd.DataFrame([[0.5, 1.0]], columns=["feature1", "feature2"])
    pd.testing.assert_frame_equal(normalized_df, expected_df)

def test_denormalize_data():
    normalized_value = 0.5
    expected_value = 27.5
    
    
    result = denormalized_data(normalized_value)
    
    assert result == expected_value, f"Expected {expected_value}, but got {result}"