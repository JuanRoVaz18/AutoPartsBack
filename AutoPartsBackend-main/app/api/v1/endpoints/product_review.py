from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.schemas.product_review import ProductReview, ProductReviewCreate
from app.api.v1.crud import product_review as crud

router = APIRouter(prefix="/product-reviews", tags=["Product Reviews"])

@router.post("/", response_model=ProductReview)
def create_product_review(review: ProductReviewCreate, db: Session = Depends(get_db)):
    return crud.create_product_review(db, review)
