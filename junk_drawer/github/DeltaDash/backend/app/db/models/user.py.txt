from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Add properties for compatibility with existing code
    @property
    def full_name(self):
        return self.username
    
    @property
    def role(self):
        return "admin" if self.is_admin else "viewer"
    
    @property
    def is_active(self):
        return True
    
    @property
    def updated_at(self):
        return self.created_at
