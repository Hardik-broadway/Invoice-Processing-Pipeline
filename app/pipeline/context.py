# app/pipeline/context.py
from dataclasses import dataclass, field
from uuid import UUID

from app.extraction.schema import ExtractionResponse


@dataclass
class PipelineContext:
    document_id: UUID
    file_path: str
    raw_text: str | None = None
    extraction_data: ExtractionResponse | None = None
    validated_data: dict | None = None
    page_images: list[str] = field(default_factory=list)
