# test_session.py

Source: junk_drawer/github/DeltaDash/backend/app/db/models/test_session.py.txt

Category: [[github-code]]

## Summary
from sqlalchemy import Column, String, Numeric, Date, DateTime, ForeignKey, func, Boolean from sqlalchemy.dialects.postgresql import UUID import uuid from app.db.base import Base class TestSession(Base): __tablename__ = "test_sessions"

## Full Content
from sqlalchemy import Column, String, Numeric, Date, DateTime, ForeignKey, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class TestSession(Base):
    __tablename__ = "test_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    test_date = Column(Date)
    lab_name = Column(String)
    operator = Column(String)
    protocol = Column(String)
    clay_temperature_c = Column(Numeric(5, 2))
    ambient_temperature_c = Column(Numeric(5, 2))
    humidity_percent = Column(Numeric(5, 2))
    conditioning = Column(String)
    size = Column(String)
    ballistic_limit = Column(Boolean, default=False)
    parent_test_group_id = Column(UUID(as_uuid=True), ForeignKey('test_sessions.id'), nullable=True)
    excel_file_path = Column(String)
    notes = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/app/db/models/test_session.py.txt
- Extracted: 2026-05-18
- Category: github-code
