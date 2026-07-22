# app/pipeline/context.py
from dataclasses import dataclass
from uuid import UUID


@dataclass
class PipelineContext:
    document_id: UUID
    file_path: str
    raw_text: str | None = None
    extraction_data: dict | None = None
    validated_data: dict | None = None
