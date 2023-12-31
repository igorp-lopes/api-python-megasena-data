from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.app.core.container import Container
from src.app.services.mega_sena_scrapper_service import MegaSenaScrapperService

router = APIRouter(prefix="/v1/data")


@router.get("/test")
@inject
async def get_api_status(
    mega_sena_scrapper_service: MegaSenaScrapperService = Depends(
        Provide[Container.mega_sena_scrapper_service]
    ),
):
    saved_value = await mega_sena_scrapper_service.test_save_mega_sena_record()
    return {"status": "OK"}
