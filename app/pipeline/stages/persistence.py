# app/pipeline/stages/persistence.py
import logging
from app.db.uow import UnitOfWork
from app.extraction.model import DocumentExtraction
from app.pipeline.context import PipelineContext


logger = logging.getLogger(__name__)


class PersistenceStage:
    async def execute(
        self,
        context: PipelineContext,
        uow: UnitOfWork,
    ):
        logger.info("Starting persistence stage")
        existing = await uow.extractions.get_by_document_id(context.document_id)
        if context.extraction_data is None:
            raise ValueError("Extraction data is None.")

        if existing:
            existing.raw_text = context.raw_text
            existing.extraction_data = context.extraction_data.model_dump()
            existing.validated_data = context.validated_data
            await uow.extractions.update(existing)
            return

        extraction = DocumentExtraction(
            document_id=context.document_id,
            raw_text=context.raw_text,
            extraction_data=context.extraction_data.model_dump(),
            validated_data=context.validated_data,
        )

        await uow.extractions.create(extraction)
        logger.info("Persistence stage completed")
