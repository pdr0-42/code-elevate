from fastapi import APIRouter

health_router = APIRouter(prefix='/health', tags=['health'])


@health_router.get('/ping')
async def ping():
    """
    Endpoint to check if the API is responding correctly.
    
    Returns a simple dictionary with the key 'ping' and the value 'pong' 
    to indicate that the API is functioning.

    Returns:
        dict: Contains the key 'ping' with the value 'pong'.
    """
    return {'ping': 'pong'}
