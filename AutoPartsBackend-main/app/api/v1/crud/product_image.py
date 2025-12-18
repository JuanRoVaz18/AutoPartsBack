from sqlalchemy.orm import Session
from app.api.v1.models.product_image import ProductImage
from app.api.v1.schemas.product_image import ProductImageCreate


def create_product_image(db: Session, product_image: ProductImageCreate):
    db_product_image = ProductImage(
        product_id=product_image.product_id,
        image_id=product_image.image_id
    )
    db.add(db_product_image)
    db.commit()
    return db_product_image


def get_product_images(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(ProductImage)
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_product_image(db: Session, product_id: int, image_id: int):
    db_product_image = (
        db.query(ProductImage)
        .filter(
            ProductImage.product_id == product_id,
            ProductImage.image_id == image_id
        )
        .first()
    )

    if not db_product_image:
        return None

    db.delete(db_product_image)
    db.commit()
    return db_product_image
