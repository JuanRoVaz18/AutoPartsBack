from pydantic import BaseModel

class OrderCouponBase(BaseModel):
    order_id: int
    coupon_id: int

class OrderCouponCreate(OrderCouponBase):
    pass

class OrderCoupon(OrderCouponBase):
    class Config:
        orm_mode = True
