#app/document/router.py
from fastapi import APIRouter, Depends, File, UploadFile, status
from app.dependencies.document import get_document_service
from app.document.schema import DocumentResponse
from app.document.service import DocumentService

router = APIRouter()


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: UploadFile = File(...),
    service: DocumentService = Depends(get_document_service),
):

    return await service.upload_document(file)
