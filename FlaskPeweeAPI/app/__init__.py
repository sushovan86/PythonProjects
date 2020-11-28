import peewee as pw
from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, pre_load, post_dump
from marshmallow_peewee import ModelSchema

from config import *

application = Flask(__name__)
application.config.from_object('config')

ma = Marshmallow(application)
db = pw.PostgresqlDatabase(DATABASE_USERNAME,
                           host=DATABASE_HOST,
                           user=DATABASE_USERNAME,
                           password=DATABASE_PASSWORD)


class BaseModel(pw.Model):
    class Meta:
        database = db


class BaseScheme(ModelSchema):

    @pre_load(pass_many=True)
    def unwrap(self, data, many):
        if PAYLOAD_WRAPPER not in data:
            raise ValidationError(f'Payload is not wrapped in {PAYLOAD_WRAPPER}')
        return data["data"]

    @post_dump(pass_many=True)
    def unwrap(self, data, many):
        return {PAYLOAD_WRAPPER: data}


from app.product.controller import product_route

application.register_blueprint(product_route, url_prefix="/product")
