from pydantic import BaseModel
from datetime import datetime

# ===== CREATE =====
class StatusCreate(BaseModel):
    name: str


# ===== RESPONSE =====
class Status(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
