from app.customer.controller import customer_route
from app.product.controller import product_route


def register(application):
    application.register_blueprint(product_route, url_prefix="/product")
    application.register_blueprint(customer_route, url_prefix="/customer")
