from sqlalchemy.orm import Session
from app.api.v1.models.product import Product
from app.api.v1.schemas.product import ProductCreate

# CREATE
def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        brand_id=product.brand_id,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# READ ONE
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# READ ALL
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(Product)
        .offset(skip)
        .limit(limit)
        .all()
    )


# UPDATE
def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.stock = product.stock
    db_product.brand_id = product.brand_id
    db_product.category_id = product.category_id

    db.commit()
    db.refresh(db_product)
    return db_product


# DELETE
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        return None

    db.delete(db_product)
    db.commit()
    return db_product
