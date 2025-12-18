from sqlalchemy.orm import Session
from app.api.v1.models import product_establishment as model
from app.api.v1.schemas import product_establishment as schema

def create_product_establishment(db: Session, product_establishment: schema.ProductEstablishmentCreate):
    db_product_establishment = model.ProductEstablishment(
        product_id=product_establishment.product_id,
        establishment_id=product_establishment.establishment_id
    )
    db.add(db_product_establishment)
    db.commit()
    db.refresh(db_product_establishment)
    return db_product_establishment

def get_product_establishment(db: Session, product_establishment_id: int):
    return db.query(model.ProductEstablishment).filter(model.ProductEstablishment.id == product_establishment_id).first()

def get_product_establishments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ProductEstablishment).offset(skip).limit(limit).all()

def update_product_establishment(db: Session, product_establishment_id: int, product_establishment: schema.ProductEstablishmentCreate):
    db_product_establishment = db.query(model.ProductEstablishment).filter(model.ProductEstablishment.id == product_establishment_id).first()
    if db_product_establishment:
        db_product_establishment.product_id = product_establishment.product_id
        db_product_establishment.establishment_id = product_establishment.establishment_id
        db.commit()
        db.refresh(db_product_establishment)
        return db_product_establishment
    return None

def delete_product_establishment(db: Session, product_establishment_id: int):
    db_product_establishment = db.query(model.ProductEstablishment).filter(model.ProductEstablishment.id == product_establishment_id).first()
    if db_product_establishment:
        db.delete(db_product_establishment)
        db.commit()
        return db_product_establishment
    return None
