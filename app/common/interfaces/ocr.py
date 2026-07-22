# app/common/interfaces/ocr.py
from abc import ABC, abstractmethod


class OCRProvider(ABC):
    @abstractmethod
    async def extract_text(
        self,
        file_path: str,
    ) -> str:
        """Extract text from the given file path using OCR."""
        ...
