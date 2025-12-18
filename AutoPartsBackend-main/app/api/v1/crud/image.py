from sqlalchemy.orm import Session
from app.api.v1.models.image import Image as ImageModel
from app.api.v1.schemas.image import ImageCreate, ImageUpdate

def create_image(db: Session, image: ImageCreate) -> ImageModel:
    db_image = ImageModel(**image.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_images(db: Session):
    return db.query(ImageModel).all()

def get_image(db: Session, image_id: int):
    return db.query(ImageModel).filter(ImageModel.id == image_id).first()

def update_image(db: Session, image_id: int, image: ImageUpdate):
    db_image = get_image(db, image_id)
    if not db_image:
        return None

    for key, value in image.model_dump(exclude_unset=True).items():
        setattr(db_image, key, value)

    db.commit()
    db.refresh(db_image)
    return db_image

def delete_image(db: Session, image_id: int) -> bool:
    db_image = get_image(db, image_id)
    if not db_image:
        return False

    db.delete(db_image)
    db.commit()
    return True
