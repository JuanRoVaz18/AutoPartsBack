from sqlalchemy.orm import Session
from app.api.v1.models import wishlist as model
from app.api.v1.schemas import wishlist as schema

def create_wishlist(db: Session, wishlist: schema.WishlistCreate):
    db_wishlist = model.Wishlist(
        user_id=wishlist.user_id
    )
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist

def get_wishlist(db: Session, wishlist_id: int):
    return db.query(model.Wishlist).filter(model.Wishlist.id == wishlist_id).first()

def get_wishlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Wishlist).offset(skip).limit(limit).all()

def delete_wishlist(db: Session, wishlist_id: int):
    db_wishlist = db.query(model.Wishlist).filter(model.Wishlist.id == wishlist_id).first()
    if db_wishlist:
        db.delete(db_wishlist)
        db.commit()
        return db_wishlist
    return None
