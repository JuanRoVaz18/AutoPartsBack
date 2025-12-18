from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class OrderCoupon(Base):
    __tablename__ = "order_coupon"

    order_id = Column(Integer, ForeignKey("order.id"), primary_key=True)
    coupon_id = Column(Integer, ForeignKey("coupon.id"), primary_key=True)
