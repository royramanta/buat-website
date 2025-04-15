from flask import Blueprint, request, jsonify
from config import db
from models import Product
# from functools import wraps
# import jwt
# import datetime

routes = Blueprint('routes', __name__)

# Get all products
@routes.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

# Add product
@routes.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product Added!", "Product": new_product.to_dict()}), 201

# Update product berdasarkan ID
@routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.stock = data['stock']
    db.session.commit()
    return jsonify({"message": "Product Updated!", "Product": product.to_dict()})

# Delete product berdasarkan ID
@routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product Deleted!"})

