from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class ProductCharacteristic(Base):
    __tablename__ = "product_characteristic"

    id = Column(Integer, primary_key=True, index=True)

    characteristic_name = Column(String, nullable=False)
    characteristic_value = Column(String, nullable=False)

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
