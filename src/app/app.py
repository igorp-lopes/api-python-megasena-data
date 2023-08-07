from fastapi import FastAPI

from src.app.controllers import health_controller
from src.app.core.container import Container


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()

    app.container = container
    app.include_router(health_controller.router)

    return app
