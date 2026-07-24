# app/core/lifespan.py
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()

    logger = structlog.get_logger()

    logger.info("Application starting")

    yield

    logger.info("Application shutting down")
