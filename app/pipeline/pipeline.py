# app/pipeline/pipeline.py
from app.core.config import settings
from app.db.uow import UnitOfWork
from app.integrations.llm.gemini_provider import GeminiProvider
from app.integrations.ocr.pdfplumber_provider import PDFPlumberOCRProvider
from app.integrations.pdf_renderer.pymupdf_renderer import PyMuPDFRenderer
from app.pipeline.context import PipelineContext
from app.pipeline.stages.extraction import ExtractionStage
from app.pipeline.stages.ocr import OCRStage
from app.pipeline.stages.persistence import PersistenceStage
from app.pipeline.stages.render import RenderStage


class DocumentPipeline:
    def __init__(self):
        ocr_provider = PDFPlumberOCRProvider()
        provider = GeminiProvider(api_key=settings.GEMINI_API_KEY)
        self.stages = [
            OCRStage(ocr_provider),
            RenderStage(renderer=PyMuPDFRenderer()),
            ExtractionStage(provider),
            PersistenceStage(),
        ]

    async def process(
        self,
        context: PipelineContext,
        uow: UnitOfWork,
    ):

        for stage in self.stages:
            await stage.execute(
                context=context,
                uow=uow,
            )
