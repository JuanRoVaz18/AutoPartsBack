from pydantic import BaseModel
from datetime import datetime

# ====== CREATE ======
class LogCreate(BaseModel):
    action: str


# ====== RESPONSE ======
class Log(BaseModel):
    id: int
    action: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2
