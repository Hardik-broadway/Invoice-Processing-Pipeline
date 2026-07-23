# app/common/interfaces/llm.py
from abc import ABC, abstractmethod

from app.extraction.schema import ExtractionResponse


class LLMProvider(ABC):
    @abstractmethod
    async def extract_invoice(
        self,
        raw_text: str,
    ) -> ExtractionResponse:
        pass
