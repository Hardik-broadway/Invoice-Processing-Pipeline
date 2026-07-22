from dataclasses import dataclass
from uuid import UUID

from app.document.model import Document


@dataclass
class PipelineContext:

    document: Document

    document_id: UUID

    raw_text: str | None = None

    supplier_name: str | None = None

    supplier_address: str | None = None

    validated_address: str | None = None

    latitude: float | None = None

    longitude: float | None = None