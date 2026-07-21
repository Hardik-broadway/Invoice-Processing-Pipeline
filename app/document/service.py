from fastapi import UploadFile

from app.common.interfaces.repository import DocumentRepositoryInterface
from app.common.interfaces.storage import Storage
from app.document.model import Document


class DocumentService:
    def __init__(
        self,
        repository: DocumentRepositoryInterface,
        storage: Storage,
    ):
        self.document_repository = repository
        self.storage = storage

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

        return await self.document_repository.create(document)
