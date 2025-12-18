from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import product_attribute as crud
from app.api.v1.schemas import product_attribute as schema
from app.core.database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=schema.ProductAttribute)
def create_product_attribute(
    attribute: schema.ProductAttributeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product_attribute(db=db, data=attribute)


@router.get("/{attribute_id}", response_model=schema.ProductAttribute)
def read_product_attribute(
    attribute_id: int,
    db: Session = Depends(get_db)
):
    db_attribute = crud.get_product_attribute(db=db, attribute_id=attribute_id)
    if not db_attribute:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return db_attribute


@router.get("/", response_model=List[schema.ProductAttribute])
def read_product_attributes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_product_attributes(db=db, skip=skip, limit=limit)


@router.put("/{attribute_id}", response_model=schema.ProductAttribute)
def update_product_attribute(
    attribute_id: int,
    attribute: schema.ProductAttributeCreate,
    db: Session = Depends(get_db)
):
    db_attribute = crud.update_product_attribute(
        db=db,
        attribute_id=attribute_id,
        data=attribute
    )
    if not db_attribute:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return db_attribute


@router.delete("/{attribute_id}", response_model=schema.ProductAttribute)
def delete_product_attribute(
    attribute_id: int,
    db: Session = Depends(get_db)
):
    db_attribute = crud.delete_product_attribute(db=db, attribute_id=attribute_id)
    if not db_attribute:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return db_attribute
