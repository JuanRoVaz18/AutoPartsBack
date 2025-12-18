from sqlalchemy.orm import Session
from app.api.v1.models.order_coupon import OrderCoupon
from app.api.v1.schemas.order_coupon import OrderCouponCreate


# CREATE
def create_order_coupon(db: Session, order_coupon: OrderCouponCreate):
    db_order_coupon = OrderCoupon(
        order_id=order_coupon.order_id,
        coupon_id=order_coupon.coupon_id
    )
    db.add(db_order_coupon)
    db.commit()
    return db_order_coupon


# READ ALL
def get_order_coupons(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(OrderCoupon)
        .offset(skip)
        .limit(limit)
        .all()
    )


# READ ONE (PK COMPUESTA)
def get_order_coupon(db: Session, order_id: int, coupon_id: int):
    return (
        db.query(OrderCoupon)
        .filter(
            OrderCoupon.order_id == order_id,
            OrderCoupon.coupon_id == coupon_id
        )
        .first()
    )


# DELETE
def delete_order_coupon(db: Session, order_id: int, coupon_id: int):
    db_order_coupon = get_order_coupon(db, order_id, coupon_id)

    if not db_order_coupon:
        return None

    db.delete(db_order_coupon)
    db.commit()
    return db_order_coupon
