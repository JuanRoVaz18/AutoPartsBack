from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import product_image as crud
from app.api.v1.schemas import product_image as schema
from app.core.database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=schema.ProductImage)
def create_product_image(
    product_image: schema.ProductImageCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product_image(db=db, product_image=product_image)


@router.get("/", response_model=List[schema.ProductImage])
def read_product_images(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_product_images(db=db, skip=skip, limit=limit)


@router.delete("/", response_model=schema.ProductImage)
def delete_product_image(
    product_id: int,
    image_id: int,
    db: Session = Depends(get_db)
):
    db_product_image = crud.delete_product_image(
        db=db,
        product_id=product_id,
        image_id=image_id
    )

    if not db_product_image:
        raise HTTPException(status_code=404, detail="ProductImage not found")

    return db_product_image
