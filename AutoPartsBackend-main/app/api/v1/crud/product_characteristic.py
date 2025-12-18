from sqlalchemy.orm import Session
from app.api.v1.models import product_characteristic as model
from app.api.v1.schemas import product_characteristic as schema


def create_product_characteristic(
    db: Session,
    characteristic: schema.ProductCharacteristicCreate
):
    db_characteristic = model.ProductCharacteristic(
        product_id=characteristic.product_id,
        characteristic_name=characteristic.characteristic_name,
        characteristic_value=characteristic.characteristic_value
    )
    db.add(db_characteristic)
    db.commit()
    db.refresh(db_characteristic)
    return db_characteristic


def get_product_characteristic(db: Session, characteristic_id: int):
    return (
        db.query(model.ProductCharacteristic)
        .filter(model.ProductCharacteristic.id == characteristic_id)
        .first()
    )


def get_product_characteristics(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(model.ProductCharacteristic)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_product_characteristic(
    db: Session,
    characteristic_id: int,
    characteristic: schema.ProductCharacteristicCreate
):
    db_characteristic = (
        db.query(model.ProductCharacteristic)
        .filter(model.ProductCharacteristic.id == characteristic_id)
        .first()
    )
    if not db_characteristic:
        return None

    db_characteristic.characteristic_name = characteristic.characteristic_name
    db_characteristic.characteristic_value = characteristic.characteristic_value

    db.commit()
    db.refresh(db_characteristic)
    return db_characteristic


def delete_product_characteristic(db: Session, characteristic_id: int):
    db_characteristic = (
        db.query(model.ProductCharacteristic)
        .filter(model.ProductCharacteristic.id == characteristic_id)
        .first()
    )
    if not db_characteristic:
        return None

    db.delete(db_characteristic)
    db.commit()
    return db_characteristic
