# app/integrations/ocr/pdfplumber_provider.py
import pdfplumber

from app.common.interfaces.ocr import OCRProvider


class PDFPlumberOCRProvider(OCRProvider):
    async def extract_text(
        self,
        file_path: str,
    ) -> str:

        pages = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    pages.append(text)

        return "\n".join(pages)
