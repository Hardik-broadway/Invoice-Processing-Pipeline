# app/integrations/llm/gemini_provider.py

import asyncio
import logging
from pathlib import Path
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
        page_images: list[str],
    ) -> ExtractionResponse:
        try:
            parts: list[types.Part] = [
                types.Part.from_text(
                    text=INVOICE_EXTRACTION_PROMPT,
                ),
                types.Part.from_text(
                    text=f"Raw OCR text:\n{raw_text}",
                ),
            ]

            for image_path in page_images:
                image_data = await self.read_image(image_path)
                parts.append(
                    types.Part.from_bytes(
                        data=image_data,
                        mime_type="image/png",
                    )
                )

            if not page_images:
                raise ValueError("No page images provided for Gemini extraction")

            logger.info(
                "Gemini request",
                extra={
                    "pages": len(page_images),
                    "page_images": page_images,
                    "ocr_characters": len(raw_text),
                },
            )

            response = await self.client.aio.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=[
                    types.Content(
                        parts=parts,
                    )
                ],
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
            logger.info(
                "Sending invoice to Gemini for extraction",
                extra={
                    "pages": len(page_images),
                    "ocr_characters": len(raw_text),
                },
            )
            raise

    @staticmethod
    async def read_image(path: str) -> bytes:
        return await asyncio.to_thread(
            Path(path).read_bytes,
        )
