from fastapi import FastAPI
from app.api.v1.endpoints import (
    product, user, category, brand, order, coupon, address,
    product_review, shopping_cart, service_request,
    product_characteristic, product_attribute, order_coupon,
    purchase_history, product_discount, user_discount,
    shopping_cart_product, review, product_image,
    product_establishment, establishment, role, order_product,
    image, log,status,role,wishlist,return_request
)
from app.core.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(category.router, prefix="/categories", tags=["categories"])
app.include_router(brand.router, prefix="/brands", tags=["brands"])
app.include_router(order.router, prefix="/orders", tags=["orders"])
app.include_router(coupon.router, prefix="/coupons", tags=["coupons"])
app.include_router(address.router, prefix="/addresses", tags=["addresses"])
#app.include_router(product_review.router, prefix="/reviews", tags=["reviews"])
app.include_router(shopping_cart.router, prefix="/shopping-carts", tags=["shopping-carts"])
app.include_router(service_request.router, prefix="/service-requests", tags=["service-requests"])
app.include_router(product_characteristic.router, prefix="/product-characteristics", tags=["product-characteristics"])
app.include_router(product_attribute.router, prefix="/product-attributes", tags=["product-attributes"])
app.include_router(order_coupon.router, prefix="/order-coupons", tags=["order-coupons"])
app.include_router(purchase_history.router, prefix="/purchase-history", tags=["purchase-history"])
app.include_router(product_discount.router, prefix="/product-discounts", tags=["product-discounts"])
app.include_router(user_discount.router, prefix="/user-discounts", tags=["user-discounts"])
app.include_router(shopping_cart_product.router, prefix="/shopping-cart-products", tags=["shopping-cart-products"])

app.include_router(product_image.router, prefix="/product-images", tags=["product-images"])
app.include_router(product_establishment.router, prefix="/product-establishments", tags=["product-establishments"])
app.include_router(establishment.router, prefix="/establishments", tags=["establishments"])
app.include_router(role.router, prefix="/roles", tags=["roles"])
app.include_router(order_product.router, prefix="/order-products", tags=["order-products"])

#---CORREGIDAS Y AGREGADAS----
app.include_router(image.router)
app.include_router(log.router)
app.include_router(status.router)
app.include_router(role.router)
app.include_router(review.router)
app.include_router(wishlist.router, prefix="/wishlists", tags=["wishlists"])
app.include_router(
    return_request.router,
    prefix="/return-requests",
    tags=["Return Requests"]
)