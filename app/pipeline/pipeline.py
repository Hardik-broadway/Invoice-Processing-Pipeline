from app.pipeline.context import PipelineContext
from app.pipeline.stages.extraction import ExtractionStage
from app.pipeline.stages.ocr import OCRStage
from app.pipeline.stages.validation import ValidationStage


class DocumentPipeline:
    def __init__(self):

        self.stages = [
            OCRStage(),
            ExtractionStage(),
            ValidationStage(),
        ]

    async def process(
        self,
        context: PipelineContext,
    ):

        for stage in self.stages:
            await stage.execute(context)
