# app/workers/document_worker.py
from uuid import UUID

from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.uow import UnitOfWork
from app.pipeline.context import PipelineContext
from app.pipeline.pipeline import DocumentPipeline


class DocumentWorker:
    def __init__(
        self,
        session_factory: async_sessionmaker,
    ):
        self.session_factory = session_factory
        self.pipeline = DocumentPipeline()

    async def process(
        self,
        document_id: UUID,
    ):

        async with self.session_factory() as session:
            uow = UnitOfWork(session)

            document = await uow.documents.get_by_id(document_id)

            if document is None:
                raise ValueError(f"Document {document_id} not found")

            context = PipelineContext(
                document_id=document.id,
                file_path=f"uploads/{document.stored_filename}",
            )

            await self.pipeline.process(
                context=context,
                uow=uow,
            )

            await uow.commit()
