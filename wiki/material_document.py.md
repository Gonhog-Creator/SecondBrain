# material_document.py

Source: junk_drawer/github/DeltaDash/backend/app/db/models/material_document.py.txt

Category: [[github-code]]

## Summary
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, func from sqlalchemy.dialects.postgresql import UUID import uuid from app.db.base import Base class MaterialDocument(Base): __tablename__ = "material_documents"

## Full Content
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class MaterialDocument(Base):
    __tablename__ = "material_documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    material_id = Column(UUID(as_uuid=True), ForeignKey("materials.id"), nullable=True)
    document_type = Column(String)
    original_filename = Column(String, nullable=False)
    stored_path = Column(String, nullable=False)
    parsed_text = Column(String)
    manufacturer_detected = Column(String)
    extraction_confidence = Column(Numeric(5, 4))
    uploaded_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/app/db/models/material_document.py.txt
- Extracted: 2026-05-18
- Category: github-code
