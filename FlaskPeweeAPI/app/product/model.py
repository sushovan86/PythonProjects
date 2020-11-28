import peewee as pw
from marshmallow import fields
from marshmallow_peewee import ModelSchema

from app import BaseModel


class Product(BaseModel):
    id = pw.AutoField(column_name="id", primary_key=True)
    company = pw.CharField(column_name="company")
    product_description = pw.CharField(column_name="productdescription")
    price = pw.FloatField(column_name="price")


class ProductSchema(ModelSchema):
    class Meta:
        model = Product

    description = fields.Str(data_key="description")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
