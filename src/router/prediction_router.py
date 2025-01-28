from http import HTTPStatus
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..preprocessing.normalize import normalize_data
from ..model.schema import Request
from ..model.model import model

prediction_router = APIRouter(prefix='/prediction', tags=['prediction'])


@prediction_router.post('/house_price', status_code=HTTPStatus.CREATED)
async def predict_house_price(request: Request):
    """
    Endpoint to predict house prices.

    This endpoint takes a request with house features, normalizes the data,
    and returns the predicted house price.

    Parameters
    ----------
    request : Request
        A Pydantic model containing the input data for the prediction.

    Returns
    -------
    JSONResponse
        A JSON response containing the predicted house price.
    """
    normalized_data = normalize_data(request)
    return JSONResponse(
        media_type='application/json',
        status_code=HTTPStatus.CREATED,
        content={'prediction': model.predict(normalized_data)},
    )
