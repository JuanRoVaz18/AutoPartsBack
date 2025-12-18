from sqlalchemy.orm import Session
from app.api.v1.models import user_discount as model
from app.api.v1.schemas import user_discount as schema

def create_user_discount(db: Session, user_discount: schema.UserDiscountCreate):
    db_user_discount = model.UserDiscount(
        name=user_discount.name,
        discount=user_discount.discount,
        start_date=user_discount.start_date,
        end_date=user_discount.end_date,
        user_id=user_discount.user_id
    )
    db.add(db_user_discount)
    db.commit()
    db.refresh(db_user_discount)
    return db_user_discount

def get_user_discount(db: Session, user_discount_id: int):
    return db.query(model.UserDiscount).filter(model.UserDiscount.id == user_discount_id).first()

def get_user_discounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.UserDiscount).offset(skip).limit(limit).all()

def update_user_discount(db: Session, user_discount_id: int, user_discount: schema.UserDiscountCreate):
    db_user_discount = db.query(model.UserDiscount).filter(model.UserDiscount.id == user_discount_id).first()
    if not db_user_discount:
        return None

    db_user_discount.name = user_discount.name
    db_user_discount.discount = user_discount.discount
    db_user_discount.start_date = user_discount.start_date
    db_user_discount.end_date = user_discount.end_date
    db_user_discount.user_id = user_discount.user_id

    db.commit()
    db.refresh(db_user_discount)
    return db_user_discount

def delete_user_discount(db: Session, user_discount_id: int):
    db_user_discount = db.query(model.UserDiscount).filter(model.UserDiscount.id == user_discount_id).first()
    if not db_user_discount:
        return None

    db.delete(db_user_discount)
    db.commit()
    return db_user_discount
