from dependency_injector import containers, providers

from src.app.adapters.sqlalchemy.repository.mega_sena_record_repository import (
    MegaSenaRecordRepository,
)
from src.app.adapters.sqlalchemy.repository.sql_alchemy_session_factory import (
    SqlAlchemySessionFactory,
)
from src.app.core.config import DATABASE_URL
from src.app.services.mega_sena_data_service import MegaSenaDataService
from src.app.services.mega_sena_scrapper_service import MegaSenaScrapperService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["src.app.controllers.health_controller", "src.cron_job.test_cron"]
    )

    session_factory = providers.Singleton(SqlAlchemySessionFactory, db_url=DATABASE_URL)

    mega_sena_record_repository = providers.Factory(
        MegaSenaRecordRepository, session_factory=session_factory.provided.session
    )

    mega_sena_data_service = providers.Factory(
        MegaSenaDataService, mega_sena_data_repository=mega_sena_record_repository
    )

    mega_sena_scrapper_service = providers.Factory(
        MegaSenaScrapperService, mega_sena_data_service=mega_sena_data_service
    )
