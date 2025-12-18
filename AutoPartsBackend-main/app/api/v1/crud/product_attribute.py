from sqlalchemy.orm import Session
from app.api.v1.models import product_attribute as model
from app.api.v1.schemas import product_attribute as schema


def create_product_attribute(
    db: Session,
    data: schema.ProductAttributeCreate
):
    db_attribute = model.ProductAttribute(
        product_id=data.product_id,
        attribute_name=data.attribute_name,
        attribute_value=data.attribute_value
    )
    db.add(db_attribute)
    db.commit()
    db.refresh(db_attribute)
    return db_attribute


def get_product_attribute(db: Session, attribute_id: int):
    return (
        db.query(model.ProductAttribute)
        .filter(model.ProductAttribute.id == attribute_id)
        .first()
    )


def get_product_attributes(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(model.ProductAttribute)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_product_attribute(
    db: Session,
    attribute_id: int,
    data: schema.ProductAttributeCreate
):
    db_attribute = (
        db.query(model.ProductAttribute)
        .filter(model.ProductAttribute.id == attribute_id)
        .first()
    )
    if not db_attribute:
        return None

    db_attribute.attribute_name = data.attribute_name
    db_attribute.attribute_value = data.attribute_value
    db.commit()
    db.refresh(db_attribute)
    return db_attribute


def delete_product_attribute(db: Session, attribute_id: int):
    db_attribute = (
        db.query(model.ProductAttribute)
        .filter(model.ProductAttribute.id == attribute_id)
        .first()
    )
    if not db_attribute:
        return None

    db.delete(db_attribute)
    db.commit()
    return db_attribute
