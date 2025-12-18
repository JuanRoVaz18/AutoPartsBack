from sqlalchemy.orm import Session
from app.api.v1.models.product_review import ProductReview
from app.api.v1.schemas.product_review import ProductReviewCreate

def create_product_review(db: Session, review: ProductReviewCreate):
    db_review = ProductReview(
        product_id=review.product_id,
        review_id=review.review_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
