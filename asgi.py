import uvicorn
from pydantic_settings import BaseSettings
from src.app.main import app


class ServiceSettings(BaseSettings):
    APP: str = "src.app.main:app"
    HOST: str = "0.0.0.0"
    PORT: int = 8084

settings = ServiceSettings()


if __name__ == "__main__":
    uvicorn.run(settings.APP, host=settings.HOST, port=settings.PORT)