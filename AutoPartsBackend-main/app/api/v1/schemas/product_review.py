from pydantic import BaseModel
from datetime import datetime

class ProductReviewCreate(BaseModel):
    product_id: int
    review_id: int


class ProductReview(BaseModel):
    id: int
    product_id: int
    review_id: int
    created_at: datetime

    class Config:
        from_attributes = True
