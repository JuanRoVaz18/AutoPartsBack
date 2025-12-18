from sqlalchemy import Column, Integer, DateTime, Date, ForeignKey
from datetime import datetime
from app.core.database import Base

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(Date, default=datetime.utcnow)
