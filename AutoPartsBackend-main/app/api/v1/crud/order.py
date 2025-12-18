from sqlalchemy.orm import Session
from app.api.v1.models import order as model
from app.api.v1.schemas import order as schema

def create_order(db: Session, order: schema.OrderCreate):
    db_order = model.Order(
        order_reference=order.order_reference,
        payment_method=order.payment_method,
        shipping_address=order.shipping_address,
        payment_status=order.payment_status,
        shipping_method=order.shipping_method,
        user_id=order.user_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
