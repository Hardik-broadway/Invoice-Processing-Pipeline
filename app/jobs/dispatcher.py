# app/jobs/dispatcher.py
from abc import ABC, abstractmethod
from uuid import UUID


class JobDispatcher(ABC):
    @abstractmethod
    async def dispatch_document(
        self,
        document_id: UUID,
    ) -> None:
        pass
