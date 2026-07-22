from sqlalchemy.ext.asyncio import AsyncSession
from app.document_extraction.model import DocumentExtraction


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
