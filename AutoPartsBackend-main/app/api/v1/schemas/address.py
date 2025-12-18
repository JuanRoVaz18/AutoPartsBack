from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ===== BASE =====
class AddressBase(BaseModel):
    name: str
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    postal_code: str
    country: str
    user_id: int

# ===== CREATE =====
class AddressCreate(AddressBase):
    pass

# ===== RESPONSE =====
class Address(AddressBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
