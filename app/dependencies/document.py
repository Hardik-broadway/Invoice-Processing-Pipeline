from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.document.repository import DocumentRepository
from app.document.service import DocumentService
from app.storage.local_storage import LocalStorage
from app.workers.document_worker import DocumentWorker


def get_document_service(
    db: AsyncSession = Depends(get_db),
) -> DocumentService:

    repository = DocumentRepository(db)

    storage = LocalStorage()

    worker = DocumentWorker()

    return DocumentService(
        repository,
        storage,
        worker,
    )
