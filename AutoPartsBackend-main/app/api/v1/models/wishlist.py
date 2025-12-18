from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from app.core.database import Base

class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)

    added_at = Column(DateTime, default=datetime.utcnow)
