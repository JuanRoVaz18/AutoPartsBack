from pydantic import BaseModel
from datetime import datetime

class PurchaseHistoryBase(BaseModel):
    name: str
    purchase_date: datetime
    order_id: int

class PurchaseHistoryCreate(PurchaseHistoryBase):
    pass

class PurchaseHistory(PurchaseHistoryBase):
    id: int

    class Config:
        orm_mode = True
