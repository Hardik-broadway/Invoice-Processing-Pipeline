from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.health import router as health_router
from app.core.lifespan import lifespan

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(health_router, prefix=settings.API_PREFIX)
app.router.lifespan_context = lifespan
