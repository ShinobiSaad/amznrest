from flask import Blueprint, jsonify, request
from sqlalchemy import func
import api.crud as crud

api = Blueprint('api', __name__)

@api.route('/products', methods=['GET'])
def get_products(): 
    brand = request.args.get('brand', None)
    min_price = request.args.get('min_price', type=float, default=None)
    max_price = request.args.get('max_price', type=float, default=None)
    min_rating = request.args.get('min_rating', type=float)
    max_rating = request.args.get('max_rating', type=float)
    page = request.args.get('page', type=int, default=1)
    limit = request.args.get('limit', type=int, default=10)
    sort = request.args.get('sort', default=None)

    resp = crud.get_products(brand=brand, min_price=min_price, max_price=max_price, min_rating=min_rating, max_rating=max_rating, page=page, limit=limit, sort=sort)
    return {"products": resp}

@api.route('/products/top', methods=['GET'])
def get_top_products():
    resp = crud.get_top_products()
    return {"products": resp}

@api.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_product_reviews(product_id):
    page = request.args.get('page', 1, type=int)  
    limit = request.args.get('limit', 10, type=int)  

    resp = crud.get_product_with_reviews(product_id, page=page, limit=limit)
    return {"reviews": resp}