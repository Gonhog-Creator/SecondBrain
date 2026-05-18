# audit_log.py

Source: junk_drawer/github/DeltaDash/backend/app/db/models/audit_log.py.txt

Category: [[github-code]]

## Summary
from sqlalchemy import Column, String, DateTime, ForeignKey, func from sqlalchemy.dialects.postgresql import UUID, JSONB import uuid from app.db.base import Base class AuditLog(Base): __tablename__ = "audit_log"

## Full Content
from sqlalchemy import Column, String, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

from app.db.base import Base


class AuditLog(Base):
    __tablename__ = "audit_log"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    action = Column(String, nullable=False)
    entity_type = Column(String)
    entity_id = Column(UUID(as_uuid=True))
    before_json = Column(JSONB)
    after_json = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/app/db/models/audit_log.py.txt
- Extracted: 2026-05-18
- Category: github-code
