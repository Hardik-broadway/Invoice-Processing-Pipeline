from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DocumentExtraction(Base):
    __tablename__ = "document_extractions"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    document_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("documents.id", ondelete="CASCADE"),
    )

    raw_text: Mapped[str | None] = mapped_column(Text)

    supplier_name: Mapped[str | None]

    supplier_address: Mapped[str | None]

    invoice_number: Mapped[str | None]

    invoice_date: Mapped[str | None]

    total_amount: Mapped[str | None]

    currency: Mapped[str | None]

    latitude: Mapped[float | None]

    longitude: Mapped[float | None]

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
