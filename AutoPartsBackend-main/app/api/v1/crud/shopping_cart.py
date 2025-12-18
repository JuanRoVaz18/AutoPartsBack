from sqlalchemy.orm import Session
from app.api.v1.models import shopping_cart as model
from app.api.v1.schemas import shopping_cart as schema

def create_shopping_cart(db: Session, cart: schema.ShoppingCartCreate):
    db_cart = model.ShoppingCart(
        user_id=cart.user_id
    )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def get_shopping_cart(db: Session, cart_id: int):
    return db.query(model.ShoppingCart).filter(model.ShoppingCart.id == cart_id).first()

def get_shopping_carts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ShoppingCart).offset(skip).limit(limit).all()

def update_shopping_cart(db: Session, cart_id: int):
    db_cart = db.query(model.ShoppingCart).filter(model.ShoppingCart.id == cart_id).first()
    if not db_cart:
        return None

    db.commit()
    db.refresh(db_cart)
    return db_cart

def delete_shopping_cart(db: Session, cart_id: int):
    db_cart = db.query(model.ShoppingCart).filter(model.ShoppingCart.id == cart_id).first()
    if not db_cart:
        return None

    db.delete(db_cart)
    db.commit()
    return db_cart
