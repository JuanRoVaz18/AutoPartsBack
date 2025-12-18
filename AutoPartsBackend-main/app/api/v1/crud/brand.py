from sqlalchemy.orm import Session
from app.api.v1.models import brand as model
from app.api.v1.schemas import brand as schema


def create_brand(db: Session, brand: schema.BrandCreate):
    db_brand = model.Brand(
        name=brand.name,
        description=brand.description,
        image_url=brand.image_url
    )
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def get_brand(db: Session, brand_id: int):
    return db.query(model.Brand).filter(model.Brand.id == brand_id).first()


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(model.Brand)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_brand(db: Session, brand_id: int, brand: schema.BrandCreate):
    db_brand = db.query(model.Brand).filter(model.Brand.id == brand_id).first()
    if not db_brand:
        return None

    db_brand.name = brand.name
    db_brand.description = brand.description
    db_brand.image_url = brand.image_url

    db.commit()
    db.refresh(db_brand)
    return db_brand


def delete_brand(db: Session, brand_id: int):
    db_brand = db.query(model.Brand).filter(model.Brand.id == brand_id).first()
    if not db_brand:
        return None

    db.delete(db_brand)
    db.commit()
    return db_brand
