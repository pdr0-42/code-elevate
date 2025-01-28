import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MODEL: str
    MLFLOW_TRACKING_URI: str = os.path


config = Config()
