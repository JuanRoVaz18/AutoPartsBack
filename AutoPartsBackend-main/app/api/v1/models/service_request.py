# app/api/v1/models/service_request.py
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class ServiceRequest(Base):
    __tablename__ = "service_request"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    establishment_id = Column(
        Integer,
        ForeignKey("establishments.id"),  
        nullable=False
    )
