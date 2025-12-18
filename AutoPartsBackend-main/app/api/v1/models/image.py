# app/api/v1/models/image.py
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
