# app/extraction/service.py
from uuid import UUID

from app.db.uow import UnitOfWork
from app.extraction.model import DocumentExtraction


class ExtractionService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_extraction_by_document_id(
        self,
        document_id: UUID,
    ) -> DocumentExtraction | None:

        extraction = await self.uow.extractions.get_by_document_id(document_id)

        return extraction
