# app/integrations/pdf_renderer/pymupdf_renderer.py
import asyncio
from pathlib import Path

import fitz


class PyMuPDFRenderer:
    def _render_sync(self, pdf_path: str) -> list[str]:
        """Synchronous helper to render PDF pages to images."""
        path = Path(pdf_path)
        output_dir = Path("uploads") / "rendered" / path.stem
        output_dir.mkdir(parents=True, exist_ok=True)

        image_paths: list[str] = []

        with fitz.open(pdf_path) as doc:
            for page_number in range(len(doc)):
                page = doc[page_number]
                pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
                image_path = output_dir / f"page_{page_number + 1}.png"
                pix.save(str(image_path))
                image_paths.append(str(image_path))

        return image_paths

    async def render(self, pdf_path: str) -> list[str]:
        """Render each page of the PDF to an image asynchronously without blocking the event loop."""
        return await asyncio.to_thread(self._render_sync, pdf_path)
