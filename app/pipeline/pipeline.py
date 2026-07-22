from app.integrations.ocr.pdfplumber_provider import PDFPlumberOCRProvider
from app.pipeline.stages.ocr import OCRStage
from app.pipeline.stages.persistence import PersistenceStage


class DocumentPipeline:
    def __init__(self):

        ocr_provider = PDFPlumberOCRProvider()

        self.stages = [
            OCRStage(ocr_provider),
            PersistenceStage(),
        ]

    async def process(
        self,
        context,
        uow,
    ):

        for stage in self.stages:
            await stage.execute(
                context=context,
                uow=uow,
            )
