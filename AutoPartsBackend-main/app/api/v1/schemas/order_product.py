from pydantic import BaseModel

class OrderProductBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int

class OrderProductCreate(OrderProductBase):
    pass

class OrderProduct(OrderProductBase):
    class Config:
        orm_mode = True
