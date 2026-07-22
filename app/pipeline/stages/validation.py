from app.pipeline.context import PipelineContext
from app.pipeline.stages.base import PipelineStage


class ValidationStage(PipelineStage):
    async def execute(
        self,
        context: PipelineContext,
    ) -> None:

        print("Validating address")

        context.latitude = -37.8136

        context.longitude = 144.9631
