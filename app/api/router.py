#app/api/router.py
from fastapi import APIRouter
from app.document.router import router as document_router

api_router = APIRouter()

api_router.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"],
)
