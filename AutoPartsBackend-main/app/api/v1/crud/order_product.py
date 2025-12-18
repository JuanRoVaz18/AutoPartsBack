from sqlalchemy.orm import Session
from app.api.v1.models.order_product import OrderProduct
from app.api.v1.schemas.order_product import OrderProductCreate


# CREATE
def create_order_product(db: Session, order_product: OrderProductCreate):
    db_order_product = OrderProduct(
        order_id=order_product.order_id,
        product_id=order_product.product_id,
        quantity=order_product.quantity
    )
    db.add(db_order_product)
    db.commit()
    return db_order_product


# READ ALL
def get_order_products(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(OrderProduct)
        .offset(skip)
        .limit(limit)
        .all()
    )


# READ ONE (PK COMPUESTA)
def get_order_product(db: Session, order_id: int, product_id: int):
    return (
        db.query(OrderProduct)
        .filter(
            OrderProduct.order_id == order_id,
            OrderProduct.product_id == product_id
        )
        .first()
    )


# UPDATE
def update_order_product(
    db: Session,
    order_id: int,
    product_id: int,
    quantity: int
):
    db_order_product = get_order_product(db, order_id, product_id)

    if not db_order_product:
        return None

    db_order_product.quantity = quantity
    db.commit()
    return db_order_product


# DELETE
def delete_order_product(db: Session, order_id: int, product_id: int):
    db_order_product = get_order_product(db, order_id, product_id)

    if not db_order_product:
        return None

    db.delete(db_order_product)
    db.commit()
    return db_order_product
