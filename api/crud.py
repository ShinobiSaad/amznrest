
from api.models import Product, Review
from sqlalchemy import or_, func, cast 
from database.db_manager import db
from sqlalchemy.types import Float

def get_products(brand=None, min_price=None, max_price=None, min_rating=None, max_rating=None, page=1, limit=10, sort=None):
    query = Product.query

    # Filter by brand
    if brand:
        query = query.filter(Product.brand.ilike(f"%{brand}%"))
    
    # Filter by price range
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    # Filter by rating range
    if min_rating is not None:
        query = query.filter(cast(Product.ratings, Float) >= float(min_rating))
    if max_rating is not None:
        query = query.filter(cast(Product.ratings, Float) <= float(max_rating))

    
    # Sorting by price: ascending or descending
    if sort == 'asc':
        query = query.order_by(Product.price.asc())
    elif sort == 'desc':
        query = query.order_by(Product.price.desc())
    # Sorting by rating: ascending or descending
    elif sort == 'rating_asc':
        query = query.order_by(cast(Product.ratings, Float).asc())
    elif sort == 'rating_desc':
        query = query.order_by(cast(Product.ratings, Float).desc())

    # Pagination: calculate offset
    offset = (page - 1) * limit
    products = query.offset(offset).limit(limit).all()

    # Response data
    resp = list()
    for product in products:
        data=dict()
        data["id"] = product.id
        data["brand"] = product.brand
        data["model"] = product.model
        data["price"] = product.price
        data["specifications"] = product.specifications
        data["ratings"] = product.ratings
        resp.append(data)
    return resp

def get_top_products(limit=10):

    products = Product.query.filter(cast(Product.ratings, Float) > 4).all()  


    resp = []
    for product in products:
        data = {
            "id": product.id,
            "brand": product.brand,
            "model": product.model,
            "price": product.price,
            "specifications": product.specifications,
            "ratings": product.ratings,
            "image_url": product.image_url,
        }
        resp.append(data)

    return resp

def get_product_with_reviews(product_id, page=1, limit=10,):
    product = Product.query.filter_by(id=product_id).first()

    if not product:
        return None  
    
    offset = (page - 1) * limit
    reviews = Review.query.filter_by(product_id=product.id).offset(offset).limit(limit).all()

    resp = list()
    for review in reviews:
        review_data = {
            "reviewer_name": review.reviewer_name,
            "review_text": review.review_text,
            "review_date": review.review_date,
            "rating": review.rating
        }
        resp.append(review_data)

    return resp