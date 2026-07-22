from fastapi import UploadFile

from app.common.interfaces.storage import Storage
from app.db.uow import UnitOfWork
from app.document.model import Document
from app.jobs.dispatcher import JobDispatcher


class DocumentService:
    def __init__(
        self,
        uow:UnitOfWork,
        storage: Storage,
        dispatcher: JobDispatcher,
    ):
        self.uow = uow
        self.storage = storage
        self.dispatcher = dispatcher

    async def upload_document(
        self,
        file: UploadFile,
    ) -> Document:

        stored_filename, file_size = await self.storage.save(file)

        document = Document(
            original_filename=file.filename or "document.pdf",
            stored_filename=stored_filename,
            content_type=file.content_type or "application/octet-stream",
            file_size=file_size,
        )

        document = await self.uow.documents.create(document)
        await self.dispatcher.dispatch_document(document.id)
        return document
