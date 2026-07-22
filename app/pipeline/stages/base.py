from abc import ABC, abstractmethod

from app.pipeline.context import PipelineContext


class PipelineStage(ABC):
    @abstractmethod
    async def execute(
        self,
        context: PipelineContext,
    ) -> None:
        pass
