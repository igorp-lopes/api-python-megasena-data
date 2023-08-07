from dependency_injector import containers, providers

from src.app.services.mega_sena_scrapper_service import MegaSenaScrapperService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["src.app.controllers.health_controller",
                 "src.cron_job.test_cron"])

    mega_sena_scrapper_service = providers.Factory(MegaSenaScrapperService)
