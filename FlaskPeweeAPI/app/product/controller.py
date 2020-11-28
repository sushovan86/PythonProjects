from flask import Blueprint
from flask import jsonify

from app.product.model import *

product_route = Blueprint("product_route", __name__)


@product_route.route("/<int:product_id>")
def get_by_id(product_id):
    prod = Product.get_or_none(Product.id == product_id)
    status_code = 200 if prod else 204

    return jsonify(product_schema.dump(prod)), status_code


@product_route.route("/by_company/<company>")
def get_by_company(company):
    product_by_company = Product.select() \
        .where(Product.company.contains(company))
    status_code = 200 if product_by_company else 204
    return jsonify(products_schema.dump(product_by_company)), status_code
