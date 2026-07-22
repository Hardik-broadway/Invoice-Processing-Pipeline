import asyncio

from app.pipeline.context import PipelineContext
from app.pipeline.pipeline import DocumentPipeline


class DocumentWorker:
    def __init__(self):
        self.pipeline = DocumentPipeline()

    async def process(
        self,
        context: PipelineContext,
    ):

        await self.pipeline.process(context)

    def dispatch(
        self,
        context: PipelineContext,
    ):

        asyncio.create_task(self.process(context))
