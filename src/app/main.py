from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router.prediction_router import prediction_router
from .health import health_router
from ..model.model import model

model.load_model()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(prediction_router)
app.include_router(health_router)
