from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(health_router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Invoice Processing Pipeline API"
    }