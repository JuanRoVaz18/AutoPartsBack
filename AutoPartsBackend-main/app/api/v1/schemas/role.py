from pydantic import BaseModel

# ===== CREATE / UPDATE =====
class RoleCreate(BaseModel):
    name: str
    description: str | None = None


# ===== RESPONSE =====
class Role(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True
