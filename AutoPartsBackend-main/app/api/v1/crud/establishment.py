from sqlalchemy.orm import Session
from app.api.v1.models import establishment as model
from app.api.v1.schemas import establishment as schema

def create_establishment(db: Session, establishment: schema.EstablishmentCreate):
    db_establishment = model.Establishment(
        name=establishment.name,
        ruc=establishment.ruc,
        city=establishment.city,
        type=establishment.type,
        email=establishment.email
    )
    db.add(db_establishment)
    db.commit()
    db.refresh(db_establishment)
    return db_establishment

def get_establishment(db: Session, establishment_id: int):
    return db.query(model.Establishment).filter(
        model.Establishment.id == establishment_id
    ).first()

def get_establishments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Establishment).offset(skip).limit(limit).all()

def update_establishment(
    db: Session,
    establishment_id: int,
    establishment: schema.EstablishmentCreate
):
    db_establishment = db.query(model.Establishment).filter(
        model.Establishment.id == establishment_id
    ).first()

    if not db_establishment:
        return None

    db_establishment.name = establishment.name
    db_establishment.ruc = establishment.ruc
    db_establishment.city = establishment.city
    db_establishment.type = establishment.type
    db_establishment.email = establishment.email

    db.commit()
    db.refresh(db_establishment)
    return db_establishment

def delete_establishment(db: Session, establishment_id: int):
    db_establishment = db.query(model.Establishment).filter(
        model.Establishment.id == establishment_id
    ).first()

    if not db_establishment:
        return None

    db.delete(db_establishment)
    db.commit()
    return db_establishment
