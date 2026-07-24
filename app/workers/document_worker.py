# app/workers/document_worker.py
from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.uow import UnitOfWork
from app.document.model import DocumentStatus
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
        """
        Process a document by its ID.
        This method retrieves the document from the database, updates its status to PROCESSING,
        executes the document processing pipeline, and updates the document's status to COMPLETED or FAILED
        based on the outcome of the processing.
        """
        async with self.session_factory() as session:
            uow = UnitOfWork(session)

            document = await uow.documents.get_by_id(document_id)

            if document is None:
                raise ValueError(f"Document {document_id} not found")

            try:
                document.status = DocumentStatus.PROCESSING
                document.error_message = None

                await uow.documents.update(document)
                await uow.commit()

                context = PipelineContext(
                    document_id=document.id,
                    file_path=f"uploads/{document.stored_filename}",
                )

                await self.pipeline.process(
                    context=context,
                    uow=uow,
                )
                document.status = DocumentStatus.COMPLETED
                document.processed_at = datetime.now(UTC)
                document.error_message = None

                await uow.documents.update(document)
                await uow.commit()

            except Exception as e:
                document.status = DocumentStatus.FAILED
                document.error_message = str(e)

                await uow.documents.update(document)
                await uow.commit()

                raise
