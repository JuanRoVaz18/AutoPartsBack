# app/api/v1/models/product.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric
from sqlalchemy.sql import func
from app.core.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    stock = Column(Integer, default=0)
    price = Column(Numeric(10, 2), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    brand_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
