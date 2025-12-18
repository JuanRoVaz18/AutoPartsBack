from sqlalchemy.orm import Session
from app.api.v1.models import coupon as model
from app.api.v1.schemas import coupon as schema

def create_coupon(db: Session, coupon: schema.CouponCreate):
    db_coupon = model.Coupon(
        code=coupon.code,
        discount_percentage=coupon.discount_percentage,
        start_date=coupon.start_date,
        end_date=coupon.end_date
    )
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon


def get_coupon(db: Session, coupon_id: int):
    return db.query(model.Coupon).filter(model.Coupon.id == coupon_id).first()

def get_coupons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Coupon).offset(skip).limit(limit).all()

def update_coupon(db: Session, coupon_id: int, coupon: schema.CouponCreate):
    db_coupon = db.query(model.Coupon).filter(model.Coupon.id == coupon_id).first()
    if db_coupon:
        db_coupon.code = coupon.code
        db_coupon.discount_percentage = coupon.discount_percentage
        db_coupon.start_date = coupon.start_date
        db_coupon.end_date = coupon.end_date
        db.commit()
        db.refresh(db_coupon)
        return db_coupon
    return None

def delete_coupon(db: Session, coupon_id: int):
    db_coupon = db.query(model.Coupon).filter(model.Coupon.id == coupon_id).first()
    if db_coupon:
        db.delete(db_coupon)
        db.commit()
        return db_coupon
    return None
