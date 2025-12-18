from sqlalchemy.orm import Session
from app.api.v1.models import shopping_cart_product as model
from app.api.v1.schemas import shopping_cart_product as schema

def create_shopping_cart_product(db: Session, shopping_cart_product: schema.ShoppingCartProductCreate):
    db_shopping_cart_product = model.ShoppingCartProduct(
        shopping_cart_id=shopping_cart_product.shopping_cart_id,
        product_id=shopping_cart_product.product_id,
        quantity=shopping_cart_product.quantity
    )
    db.add(db_shopping_cart_product)
    db.commit()
    db.refresh(db_shopping_cart_product)
    return db_shopping_cart_product

def get_shopping_cart_product(db: Session, shopping_cart_product_id: int):
    return db.query(model.ShoppingCartProduct).filter(model.ShoppingCartProduct.id == shopping_cart_product_id).first()

def get_shopping_cart_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ShoppingCartProduct).offset(skip).limit(limit).all()

def update_shopping_cart_product(db: Session, shopping_cart_product_id: int, shopping_cart_product: schema.ShoppingCartProductCreate):
    db_shopping_cart_product = db.query(model.ShoppingCartProduct).filter(model.ShoppingCartProduct.id == shopping_cart_product_id).first()
    if db_shopping_cart_product:
        db_shopping_cart_product.quantity = shopping_cart_product.quantity
        db.commit()
        db.refresh(db_shopping_cart_product)
        return db_shopping_cart_product
    return None

def delete_shopping_cart_product(db: Session, shopping_cart_product_id: int):
    db_shopping_cart_product = db.query(model.ShoppingCartProduct).filter(model.ShoppingCartProduct.id == shopping_cart_product_id).first()
    if db_shopping_cart_product:
        db.delete(db_shopping_cart_product)
        db.commit()
        return db_shopping_cart_product
    return None
