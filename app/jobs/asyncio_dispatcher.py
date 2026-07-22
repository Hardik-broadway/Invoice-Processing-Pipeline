import asyncio
from uuid import UUID

from app.jobs.dispatcher import JobDispatcher
from app.workers.document_worker import DocumentWorker


class AsyncIOJobDispatcher(JobDispatcher):
    def __init__(self):
        self.worker = DocumentWorker()

    async def dispatch_document(
        self,
        document_id: UUID,
    ) -> None:

        asyncio.create_task(self.worker.process(document_id))
