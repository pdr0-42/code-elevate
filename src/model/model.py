import mlflow
from mlflow.pyfunc import PyFuncModel
import pandas as pd
from ..app.config import config


class MlFlowModel:
    """
    A class used to load an MLflow model and make predictions.

    Attributes
    ----------
    model_path : str
        The URI of the MLflow model to be loaded.

    Methods
    -------
    load_model() -> PyFuncModel
        Loads the MLflow model from the specified model path.

    predict(data: pd.DataFrame) -> Any
        Makes predictions on the input data using the loaded MLflow model.
    """

    def __init__(self, model_path: str):
        """
        Initializes the MlFlowModel class with the specified model path.

        Parameters
        ----------
        model_path : str
            The URI of the MLflow model to be loaded.
        """
        self.model_path = model_path

    def load_model(self) -> PyFuncModel:
        """
        Loads the MLflow model from the specified model path.

        Returns
        -------
        PyFuncModel
            The loaded MLflow model.
        """
        mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)
        return mlflow.pyfunc.load_model(self.model_path)

    def predict(self, data: pd.DataFrame):
        """
        Makes predictions on the input data using the loaded MLflow model.

        Parameters
        ----------
        data : pd.DataFrame
            The input data for which predictions are to be made.

        Returns
        -------
        Any
            The prediction result for the input data.
        """
        model: PyFuncModel = self.load_model()
        return model.predict(data)[0]


model = MlFlowModel(config.MODEL)
