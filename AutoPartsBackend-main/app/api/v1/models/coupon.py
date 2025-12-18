from sqlalchemy import Column, Integer, String, DateTime, Numeric, text
from app.core.database import Base

class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), nullable=False)
    discount_percentage = Column(Numeric(10, 2), nullable=False)

    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    created_at = Column(DateTime, server_default=text('now()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('now()'), nullable=False)
