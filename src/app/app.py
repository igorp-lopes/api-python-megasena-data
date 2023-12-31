from fastapi import FastAPI

from src.app.controllers import health_controller, mega_sena_data_controller
from src.app.core.container import Container


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()

    app.container = container

    controllers = [health_controller, mega_sena_data_controller]
    for controller in controllers:
        app.include_router(controller.router)

    return app
