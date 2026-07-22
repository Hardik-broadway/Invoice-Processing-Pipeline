# app/db/uow.py
from sqlalchemy.ext.asyncio import AsyncSession

from app.document.repository import DocumentRepository
from app.extraction.repository import DocumentExtractionRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.documents = DocumentRepository(session)
        self.extractions = DocumentExtractionRepository(session)

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
