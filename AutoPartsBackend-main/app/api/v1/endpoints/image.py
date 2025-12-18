from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.schemas.image import Image, ImageCreate, ImageUpdate
from app.api.v1.crud import image as crud

router = APIRouter(prefix="/images", tags=["Images"])

@router.post("/", response_model=Image, status_code=status.HTTP_201_CREATED)
def create_image(payload: ImageCreate, db: Session = Depends(get_db)):
    return crud.create_image(db, payload)

@router.get("/", response_model=list[Image])
def list_images(db: Session = Depends(get_db)):
    return crud.get_images(db)

@router.get("/{image_id}", response_model=Image)
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image(db, image_id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.put("/{image_id}", response_model=Image)
def update_image(image_id: int, payload: ImageUpdate, db: Session = Depends(get_db)):
    db_image = crud.update_image(db, image_id, payload)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_image(db, image_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Image not found")
    return None
