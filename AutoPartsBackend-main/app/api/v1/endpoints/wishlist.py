from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.v1.crud import wishlist as crud
from app.api.v1.schemas import wishlist as schema
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=schema.Wishlist)
def create_wishlist(wishlist: schema.WishlistCreate, db: Session = Depends(get_db)):
    return crud.create_wishlist(db=db, wishlist=wishlist)

@router.get("/", response_model=List[schema.Wishlist])
def read_wishlists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_wishlists(db=db, skip=skip, limit=limit)

@router.get("/{wishlist_id}", response_model=schema.Wishlist)
def read_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    db_wishlist = crud.get_wishlist(db=db, wishlist_id=wishlist_id)
    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return db_wishlist

@router.delete("/{wishlist_id}", response_model=schema.Wishlist)
def delete_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    db_wishlist = crud.delete_wishlist(db=db, wishlist_id=wishlist_id)
    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return db_wishlist
