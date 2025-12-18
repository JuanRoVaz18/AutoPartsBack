# app/api/v1/schemas/return_request.py
from pydantic import BaseModel
from typing import Optional

class ReturnRequestBase(BaseModel):
    reason: str
    return_status: str
    order_id: int

class ReturnRequestCreate(ReturnRequestBase):
    pass

class ReturnRequest(ReturnRequestBase):
    id: int

    class Config:
        orm_mode = True
