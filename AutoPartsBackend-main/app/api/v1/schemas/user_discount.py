from pydantic import BaseModel
from datetime import datetime

# ===== BASE =====
class UserDiscountBase(BaseModel):
    name: str
    discount: int
    start_date: datetime
    end_date: datetime
    user_id: int

# ===== CREATE =====
class UserDiscountCreate(UserDiscountBase):
    pass

# ===== RESPONSE =====
class UserDiscount(UserDiscountBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
