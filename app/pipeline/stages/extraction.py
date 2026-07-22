from app.pipeline.stages.base import PipelineStage
from app.pipeline.context import PipelineContext


class ExtractionStage(PipelineStage):
    async def execute(
        self,
        context: PipelineContext,
    ) -> None:

        print("Extracting supplier")
