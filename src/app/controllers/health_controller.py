from fastapi import APIRouter

router = APIRouter(prefix="/v1")

class HealthController:
    router: APIRouter = router

    @staticmethod
    @router.get("/health")
    async def get_api_status():
        return {
            "status": "OK"
        }

