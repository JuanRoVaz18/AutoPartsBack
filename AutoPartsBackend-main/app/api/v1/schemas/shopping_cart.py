from pydantic import BaseModel
from datetime import datetime, date

# ===== BASE =====
class ShoppingCartBase(BaseModel):
    user_id: int

# ===== CREATE =====
class ShoppingCartCreate(ShoppingCartBase):
    pass

# ===== RESPONSE =====
class ShoppingCart(ShoppingCartBase):
    id: int
    created_at: datetime
    updated_at: date

    class Config:
        from_attributes = True
