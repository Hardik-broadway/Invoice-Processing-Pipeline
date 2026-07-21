from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.interfaces.repository import (
    DocumentRepositoryInterface,
)
from app.document.model import Document


class DocumentRepository(DocumentRepositoryInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        document: Document,
    ) -> Document:

        self.db.add(document)

        await self.db.commit()

        await self.db.refresh(document)

        return document

    async def get_by_id(
        self,
        document_id: UUID,
    ) -> Document | None:

        result = await self.db.execute(
            select(Document).where(Document.id == document_id)
        )

        return result.scalar_one_or_none()

    async def update(
        self,
        document: Document,
    ) -> Document:

        await self.db.commit()

        await self.db.refresh(document)

        return document
