# app/dependencies/document.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal, get_db
from app.db.uow import UnitOfWork
from app.document.service import DocumentService
from app.jobs.asyncio_dispatcher import AsyncIOJobDispatcher
from app.storage.local_storage import LocalStorage
from app.workers.document_worker import DocumentWorker


def get_document_service(
    db: AsyncSession = Depends(get_db),
) -> DocumentService:

    uow = UnitOfWork(db)

    worker = DocumentWorker(session_factory=AsyncSessionLocal)

    storage = LocalStorage()

    dispatcher = AsyncIOJobDispatcher(worker=worker)

    return DocumentService(
        uow,
        storage,
        dispatcher,
    )
