from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

# ===== BASE =====
class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    birthday: Optional[date] = None
    document_id: Optional[str] = None
    role_id: int

# ===== CREATE =====
class UserCreate(UserBase):
    password: str

# ===== RESPONSE =====
class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
