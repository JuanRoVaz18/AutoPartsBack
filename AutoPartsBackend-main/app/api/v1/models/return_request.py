# app/api/v1/models/return_request.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class ReturnRequest(Base):
    __tablename__ = "return_request"

    id = Column(Integer, primary_key=True, index=True)
    reason = Column(Text, nullable=False)
    return_status = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
