from sqlalchemy.ext.asyncio import AsyncSession

from app.document.repository import DocumentRepository
from app.document_extraction.repository import DocumentExtractionRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.documents = DocumentRepository(session)
        self.document_extractions = DocumentExtractionRepository(session)

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
