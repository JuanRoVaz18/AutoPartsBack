from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class ProductImage(Base):
    __tablename__ = "product_image"

    product_id = Column(
        Integer,
        ForeignKey("product.id"),
        primary_key=True
    )

    image_id = Column(
        Integer,
        ForeignKey("image.id"),
        primary_key=True
    )
