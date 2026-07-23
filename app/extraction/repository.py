# app/extraction/repository.py
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.extraction.model import DocumentExtraction


class DocumentExtractionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        extraction: DocumentExtraction,
    ) -> DocumentExtraction:

        self.db.add(extraction)

        await self.db.flush()

        await self.db.refresh(extraction)

        return extraction

    async def get_by_document_id(
        self,
        document_id: UUID,
    ) -> DocumentExtraction | None:

        stmt = select(DocumentExtraction).where(
            DocumentExtraction.document_id == document_id
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def update(
        self,
        extraction: DocumentExtraction,
    ) -> DocumentExtraction:

        await self.db.flush()

        await self.db.refresh(extraction)

        return extraction
