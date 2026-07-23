# app/common/interfaces/llm.py
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    async def extract_invoice(
        self,
        raw_text: str,
    ) -> dict: ...
