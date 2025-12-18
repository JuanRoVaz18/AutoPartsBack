from sqlalchemy.orm import Session
from app.api.v1.models import address as model
from app.api.v1.schemas import address as schema

def create_address(db: Session, address: schema.AddressCreate):
    db_address = model.Address(
        name=address.name,
        address_line1=address.address_line1,
        address_line2=address.address_line2,
        city=address.city,
        postal_code=address.postal_code,
        country=address.country,
        user_id=address.user_id
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_address(db: Session, address_id: int):
    return db.query(model.Address).filter(model.Address.id == address_id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Address).offset(skip).limit(limit).all()

def update_address(db: Session, address_id: int, address: schema.AddressCreate):
    db_address = db.query(model.Address).filter(model.Address.id == address_id).first()
    if not db_address:
        return None

    db_address.name = address.name
    db_address.address_line1 = address.address_line1
    db_address.address_line2 = address.address_line2
    db_address.city = address.city
    db_address.postal_code = address.postal_code
    db_address.country = address.country
    db_address.user_id = address.user_id

    db.commit()
    db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int):
    db_address = db.query(model.Address).filter(model.Address.id == address_id).first()
    if not db_address:
        return None

    db.delete(db_address)
    db.commit()
    return db_address
