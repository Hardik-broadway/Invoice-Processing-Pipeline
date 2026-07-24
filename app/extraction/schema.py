# app/extraction/schema.py
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DocumentResultResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    document_id: UUID
    raw_text: str | None = None
    extraction_data: dict | None = None
    validated_data: dict | None = None


class LineItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    item_code: str | None = None
    description: str | None = None
    model: str | None = None
    serial_number: str | None = None
    quantity: float | None = None
    unit_price: float | None = None
    gst_amount: float | None = None
    total_price: float | None = None


class Supplier(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str | None = None
    address: str | None = None


class BillTo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str | None = None
    address: str | None = None


class ShipTo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str | None = None
    address: str | None = None


class Invoice(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    invoice_number: str | None = None
    invoice_date: str | None = None
    due_date: str | None = None
    purchase_order: str | None = None
    currency: str | None = None
    total_amount: float | None = None
    gst_amount: float | None = None


class ExtractionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    supplier: Supplier | None = None
    bill_to: BillTo | None = None
    ship_to: ShipTo | None = None
    invoice: Invoice | None = None
    line_items: list[LineItem] = Field(default_factory=list)


class ExtractionListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    extractions: list[ExtractionResponse]
