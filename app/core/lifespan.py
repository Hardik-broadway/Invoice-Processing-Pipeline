from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import configure_logging
import structlog


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()

    logger = structlog.get_logger()

    logger.info("Application starting")

    yield

    logger.info("Application shutting down")
