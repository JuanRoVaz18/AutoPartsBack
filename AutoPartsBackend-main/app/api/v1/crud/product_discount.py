from sqlalchemy.orm import Session
from app.api.v1.models.product_discount import ProductDiscount
from app.api.v1.schemas.product_discount import ProductDiscountCreate


def create_product_discount(db: Session, product_discount: ProductDiscountCreate):
    db_product_discount = ProductDiscount(
        name=product_discount.name,
        description=product_discount.description,
        start_date=product_discount.start_date,
        end_date=product_discount.end_date,
        product_id=product_discount.product_id
    )
    db.add(db_product_discount)
    db.commit()
    db.refresh(db_product_discount)
    return db_product_discount


def get_product_discount(db: Session, product_discount_id: int):
    return (
        db.query(ProductDiscount)
        .filter(ProductDiscount.id == product_discount_id)
        .first()
    )


def get_product_discounts(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(ProductDiscount)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_product_discount(
    db: Session,
    product_discount_id: int,
    product_discount: ProductDiscountCreate
):
    db_product_discount = get_product_discount(db, product_discount_id)

    if not db_product_discount:
        return None

    db_product_discount.name = product_discount.name
    db_product_discount.description = product_discount.description
    db_product_discount.start_date = product_discount.start_date
    db_product_discount.end_date = product_discount.end_date
    db_product_discount.product_id = product_discount.product_id

    db.commit()
    db.refresh(db_product_discount)
    return db_product_discount


def delete_product_discount(db: Session, product_discount_id: int):
    db_product_discount = get_product_discount(db, product_discount_id)

    if not db_product_discount:
        return None

    db.delete(db_product_discount)
    db.commit()
    return db_product_discount
