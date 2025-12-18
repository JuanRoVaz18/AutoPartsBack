from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ===== BASE =====
class EstablishmentBase(BaseModel):
    name: str
    ruc: str
    city: str
    type: str
    email: Optional[str] = None

# ===== CREATE =====
class EstablishmentCreate(EstablishmentBase):
    pass

# ===== RESPONSE =====
class Establishment(EstablishmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2
