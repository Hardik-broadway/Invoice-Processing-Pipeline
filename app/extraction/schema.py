from pydantic import BaseModel, ConfigDict
from uuid import UUID


class DocumentResultResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    document_id: UUID
    raw_text: str | None
    extraction_data: dict | None
    validated_data: dict | None
