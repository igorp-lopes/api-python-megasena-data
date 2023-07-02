from fastapi import FastAPI


def create_fastapi_app():

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(create_fastapi_app(), host="0.0.0.0", port=3000)
