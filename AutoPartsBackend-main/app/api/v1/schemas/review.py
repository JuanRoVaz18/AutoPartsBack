from pydantic import BaseModel
from datetime import datetime

class ReviewCreate(BaseModel):
    review: str
    rating: int

class Review(BaseModel):
    id: int
    review: str
    rating: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
