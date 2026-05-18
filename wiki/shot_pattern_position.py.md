# shot_pattern_position.py

Source: junk_drawer/github/DeltaDash/backend/app/db/models/shot_pattern_position.py.txt

Category: [[github-code]]

## Summary
from sqlalchemy import Column, String, Numeric, Integer, DateTime, ForeignKey from sqlalchemy.dialects.postgresql import UUID import uuid from app.db.base import Base class ShotPatternPosition(Base): __tablename__ = "shot_pattern_positions"

## Full Content
from sqlalchemy import Column, String, Numeric, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class ShotPatternPosition(Base):
    __tablename__ = "shot_pattern_positions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shot_pattern_id = Column(UUID(as_uuid=True), ForeignKey("shot_patterns.id", ondelete="CASCADE"), nullable=False)
    shot_number = Column(Integer, nullable=False)
    x_normalized = Column(Numeric(5, 4))
    y_normalized = Column(Numeric(5, 4))
    x_mm = Column(Numeric(10, 2))
    y_mm = Column(Numeric(10, 2))
    impact_angle_degrees = Column(Numeric(5, 2), default=0)
    location_label = Column(String)
    notes = Column(String)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/app/db/models/shot_pattern_position.py.txt
- Extracted: 2026-05-18
- Category: github-code
