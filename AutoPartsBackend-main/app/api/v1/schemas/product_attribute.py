from pydantic import BaseModel
from datetime import datetime


class ProductAttributeBase(BaseModel):
    attribute_name: str
    attribute_value: str


class ProductAttributeCreate(ProductAttributeBase):
    product_id: int


class ProductAttribute(ProductAttributeBase):
    id: int
    product_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
