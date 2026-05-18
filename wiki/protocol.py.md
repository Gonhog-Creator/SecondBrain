# protocol.py

Source: junk_drawer/github/DeltaDash/backend/app/db/models/protocol.py.txt

Category: [[github-code]]

## Summary
from sqlalchemy import Column, String from sqlalchemy.dialects.postgresql import UUID import uuid from app.db.base import Base class Protocol(Base): __tablename__ = "protocols"

## Full Content
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Protocol(Base):
    __tablename__ = "protocols"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/app/db/models/protocol.py.txt
- Extracted: 2026-05-18
- Category: github-code
