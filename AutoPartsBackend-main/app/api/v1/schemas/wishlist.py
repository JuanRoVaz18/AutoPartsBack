from pydantic import BaseModel
from datetime import datetime

class WishlistBase(BaseModel):
    user_id: int

class WishlistCreate(WishlistBase):
    pass

class Wishlist(WishlistBase):
    id: int
    added_at: datetime

    class Config:
        orm_mode = True
