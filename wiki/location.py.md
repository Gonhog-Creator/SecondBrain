# location.py

Source: junk_drawer/github/DeltaDash/backend/app/db/models/location.py.txt

Category: [[github-code]]

## Summary
from sqlalchemy import Column, String from sqlalchemy.dialects.postgresql import UUID from app.db.base import Base import uuid class Location(Base): __tablename__ = "locations" id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

## Full Content
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid


class Location(Base):
    __tablename__ = "locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    address = Column(String(500), nullable=True)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/app/db/models/location.py.txt
- Extracted: 2026-05-18
- Category: github-code
