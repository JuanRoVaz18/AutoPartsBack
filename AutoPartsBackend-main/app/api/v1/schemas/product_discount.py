from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductDiscountBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    product_id: int


class ProductDiscountCreate(ProductDiscountBase):
    pass


class ProductDiscount(ProductDiscountBase):
    id: int

    class Config:
        orm_mode = True
