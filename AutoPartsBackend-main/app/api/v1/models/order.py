# app/api/v1/models/order.py
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, text
from app.core.database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    order_reference = Column(String)
    payment_method = Column(String)
    shipping_address = Column(String)
    payment_status = Column(String)
    shipping_method = Column(String)

    # 🔑 CLAVE ABSOLUTA
    created_at = Column(
        DateTime,
        server_default=text("now()"),
        nullable=False
    )
    updated_at = Column(
        DateTime,
        server_default=text("now()"),
        nullable=False
    )

    user_id = Column(BigInteger)
