from dependency_injector.wiring import inject
from fastapi import APIRouter

router = APIRouter(prefix="/v1")

@router.get("/health")
@inject
async def get_api_status():
    return {
        "status": "OK"
    }

