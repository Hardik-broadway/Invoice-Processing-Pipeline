# app/pipeline/stages/persistence.py
from app.db.uow import UnitOfWork
from app.extraction.model import DocumentExtraction
from app.pipeline.context import PipelineContext


class PersistenceStage:
    async def execute(
        self,
        context: PipelineContext,
        uow: UnitOfWork,
    ):
        existing = await uow.extractions.get_by_document_id(context.document_id)
        if existing:
            existing.raw_text = context.raw_text
            existing.extraction_data = context.extraction_data
            existing.validated_data = context.validated_data
            await uow.extractions.update(existing)
            return

        extraction = DocumentExtraction(
            document_id=context.document_id,
            raw_text=context.raw_text,
            extraction_data=context.extraction_data,
            validated_data=context.validated_data,
        )

        await uow.extractions.create(extraction)
