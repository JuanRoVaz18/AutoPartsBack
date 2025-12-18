from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    order_reference: str
    payment_method: str
    shipping_address: str
    payment_status: str
    shipping_method: str
    user_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
