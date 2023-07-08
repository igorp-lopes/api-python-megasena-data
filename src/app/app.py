from fastapi import FastAPI

from src.app.core.container import Container


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()

    app.container = container
    app.include_router(container.health_controller().router)

    return app
