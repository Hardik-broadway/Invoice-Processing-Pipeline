# app/document/router.py
from uuid import UUID

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from app.dependencies.document import get_document_service, get_extraction_service
from app.document.schema import DocumentListResponse, DocumentResponse
from app.document.service import DocumentService
from app.extraction.service import ExtractionService
from app.document.schema import DocumentResultResponse


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


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
    status_code=status.HTTP_200_OK,
)
async def get_document_by_id(
    document_id: UUID,
    service: DocumentService = Depends(get_document_service),
):

    document = await service.get_document_by_id(document_id)

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document {document_id} not found",
        )
    return document


@router.get(
    "",
    response_model=DocumentListResponse,
    status_code=status.HTTP_200_OK,
)
async def list_documents(
    service: DocumentService = Depends(get_document_service),
):
    documents = await service.list_documents()

    return {"documents": documents}


@router.get(
    "/{document_id}/result",
    response_model=DocumentResultResponse,
    status_code=status.HTTP_200_OK,
)
async def get_document_result(
    document_id: UUID,
    extraction_service: ExtractionService = Depends(get_extraction_service),
):

    extraction = await extraction_service.get_extraction_by_document_id(document_id)

    if extraction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Extraction for document {document_id} not found",
        )

    return {
        "document_id": extraction.document_id,
        "raw_text": extraction.raw_text,
        "extraction_data": extraction.extraction_data,
        "validated_data": extraction.validated_data,
    }
