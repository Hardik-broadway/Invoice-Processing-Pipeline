# app/pipeline/stages/validation.py
from app.pipeline.context import PipelineContext
from app.pipeline.stages.base import PipelineStage


class ValidationStage(PipelineStage):
    async def execute(
        self,
        context: PipelineContext,
    ) -> None:

        print("Validating address")
