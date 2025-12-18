from sqlalchemy.orm import Session
from app.api.v1.models.review import Review as ReviewModel
from app.api.v1.schemas.review import ReviewCreate

def create_review(db: Session, review: ReviewCreate):
    db_review = ReviewModel(
        review=review.review,
        rating=review.rating
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_review(db: Session, review_id: int):
    return db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ReviewModel).offset(skip).limit(limit).all()

def update_review(db: Session, review_id: int, review: ReviewCreate):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not db_review:
        return None

    db_review.review = review.review
    db_review.rating = review.rating
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review(db: Session, review_id: int):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not db_review:
        return None

    db.delete(db_review)
    db.commit()
    return db_review
