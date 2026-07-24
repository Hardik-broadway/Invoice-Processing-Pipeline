# app/pipeline/stages/render.py

from app.db.uow import UnitOfWork
from app.integrations.pdf_renderer import pymupdf_renderer
from app.pipeline.context import PipelineContext


class RenderStage:
    def __init__(self, renderer: pymupdf_renderer.PyMuPDFRenderer):
        self.renderer = renderer

    async def execute(self, context: PipelineContext, uow: UnitOfWork):

        context.page_images = await self.renderer.render(context.file_path)
