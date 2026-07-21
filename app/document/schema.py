#app/document/schema.py
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.document.model import DocumentStatus


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    original_filename: str
    status: DocumentStatus
    created_at: datetime
