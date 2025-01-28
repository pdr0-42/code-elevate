import pandas as pd
import joblib
from ..model.schema import Request

scaler = joblib.load('scaler.joblib')


def normalize_data(request: Request) -> pd.DataFrame:
    """
    Normalize the input data using a pre-trained scaler.

    This function takes a request object, converts it to a pandas DataFrame,
    and normalizes the data using a pre-trained scaler loaded from 'scaler.joblib'.
    The normalized data is then returned as a pandas DataFrame.

    Parameters:
    request (Request): An instance of the Request class containing the data to be normalized.

    Returns:
    pd.DataFrame: A DataFrame containing the normalized data with the same columns as the input data.
    """
    data = pd.DataFrame([request.model_dump()])

    normalized_data = scaler.transform(data)

    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)

    return normalized_df
