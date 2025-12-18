from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.v1.crud import review as crud
from app.api.v1.schemas.review import Review, ReviewCreate
from app.core.database import get_db

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db=db, review=review)

@router.get("/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    db_review = crud.get_review(db=db, review_id=review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.get("/", response_model=List[Review])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_reviews(db=db, skip=skip, limit=limit)

@router.put("/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = crud.update_review(db=db, review_id=review_id, review=review)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.delete("/{review_id}", response_model=Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = crud.delete_review(db=db, review_id=review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review
