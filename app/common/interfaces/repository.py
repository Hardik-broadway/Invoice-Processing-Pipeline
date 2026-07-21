#app/common/interfaces/repository.py
from abc import ABC, abstractmethod
from uuid import UUID
from app.document.model import Document


class DocumentRepositoryInterface(ABC):
    @abstractmethod
    async def create(self, document: Document) -> Document:
        pass

    @abstractmethod
    async def get_by_id(self, document_id: UUID) -> Document | None:
        pass

    @abstractmethod
    async def update(self, document: Document) -> Document:
        pass
