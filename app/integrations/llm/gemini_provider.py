# app/integrations/llm/gemini_provider.py
import logging
from typing import cast
from google import genai
from google.genai import types

from app.common.interfaces.llm import LLMProvider
from app.extraction.schema import ExtractionResponse
from app.integrations.llm.prompts import INVOICE_EXTRACTION_PROMPT

logger = logging.getLogger(__name__)


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str, client: genai.Client | None = None):
        self.api_key = api_key
        self.client = client or genai.Client(api_key=self.api_key)

    async def extract_invoice(
        self,
        raw_text: str,
    ) -> ExtractionResponse:
        prompt = INVOICE_EXTRACTION_PROMPT.format(raw_text=raw_text)

        try:
            response = await self.client.aio.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ExtractionResponse,
                ),
            )

            if not response.text:
                raise ValueError("Received empty response from Gemini API")

            parsed = response.parsed
            if parsed is None:
                raise ValueError(
                    "Failed to parse Gemini response into ExtractionResponse"
                )
            return cast(ExtractionResponse, parsed)

        except Exception:
            logger.exception("Failed to process or validate Gemini response")
            raise
