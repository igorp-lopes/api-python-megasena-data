from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine

from src.app.adapters.sqlmodel.repositories.mega_sena_data_repository import (
    MegaSenaDataRepository,
)
from src.app.core.config import DATABASE_URL
from src.app.services.mega_sena_data_service import MegaSenaDataService
from src.app.services.mega_sena_scrapper_service import MegaSenaScrapperService


class Container(containers.DeclarativeContainer):
    db_engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))

    wiring_config = containers.WiringConfiguration(
        modules=["src.app.controllers.health_controller", "src.cron_job.test_cron"]
    )

    mega_sena_data_repository = providers.Factory(
        MegaSenaDataRepository, engine=db_engine
    )

    mega_sena_data_service = providers.Factory(
        MegaSenaDataService, mega_sena_data_repository=mega_sena_data_repository
    )

    mega_sena_scrapper_service = providers.Factory(
        MegaSenaScrapperService, mega_sena_data_service=mega_sena_data_service
    )
