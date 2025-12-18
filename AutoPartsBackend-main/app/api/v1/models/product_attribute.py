from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class ProductAttribute(Base):
    __tablename__ = "product_attribute"

    id = Column(Integer, primary_key=True, index=True)

    attribute_name = Column(String, nullable=False)
    attribute_value = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("product.id"),
        nullable=False
    )
