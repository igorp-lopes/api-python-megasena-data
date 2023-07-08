from dependency_injector import containers, providers

from src.app.controllers.health_controller import HealthController


class Container(containers.DeclarativeContainer):
    health_controller = providers.Singleton(HealthController)
