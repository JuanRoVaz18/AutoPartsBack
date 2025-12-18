from pydantic import BaseModel
from datetime import datetime


class ProductCharacteristicBase(BaseModel):
    characteristic_name: str
    characteristic_value: str


class ProductCharacteristicCreate(ProductCharacteristicBase):
    product_id: int


class ProductCharacteristic(ProductCharacteristicBase):
    id: int
    product_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
