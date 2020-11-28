from flask import Blueprint

from app.customer.model import *
from app.helpers import *

customer_route = Blueprint("customer_route", __name__)


@customer_route.route("/<int:id>")
def get_by_id(id):
    cust = Customer.get_or_none(Customer.id == id)
    status = 200 if cust else 204
    return wrap(customer_schema.dump(cust)), status


@customer_route.route("/by_user/<username>")
def get_by_username(username):
    customers = Customer.select(Customer).where(Customer.username.contains(username))
    status = 200 if customers else 204
    return wrap(customers_schema.dump(customers)), status
