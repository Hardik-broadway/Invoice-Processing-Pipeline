from app.common.interfaces.ocr import OCRProvider
from app.db.uow import UnitOfWork
from app.pipeline.context import PipelineContext
from app.pipeline.stages.base import PipelineStage
import structlog

logger = structlog.get_logger()


class OCRStage(PipelineStage):
    def __init__(self, provider: OCRProvider):
        self.provider = provider

    async def execute(self, context: PipelineContext, uow: UnitOfWork) -> None:
        logger.info("Starting OCR", document_id=context.document_id)
        context.raw_text = await self.provider.extract_text(context.file_path)
        logger.info("OCR finished", characters=len(context.raw_text))
