# app/pipeline/stages/extraction.py
import logging
from app.common.interfaces.llm import LLMProvider
from app.db.uow import UnitOfWork
from app.pipeline.context import PipelineContext


logger = logging.getLogger(__name__)


class ExtractionStage:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    async def execute(
        self,
        context: PipelineContext,
        uow: UnitOfWork,
    ):
        if context.raw_text is None:
            raise ValueError("OCR returned no text.")

        logger.info("Starting Gemini extraction")

        context.extraction_data = await self.provider.extract_invoice(context.raw_text)
        
        logger.info("Gemini extraction completed")
