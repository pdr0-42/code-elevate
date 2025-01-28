import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MODEL: str
    MLFLOW_TRACKING_URI: str

config = Config(
    MODEL=os.getenv("MODEL", "default_model_path"),
    MLFLOW_TRACKING_URI=os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
)
