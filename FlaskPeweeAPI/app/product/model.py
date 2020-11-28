import peewee as pw
from marshmallow import fields

from app import BaseModel, BaseScheme


class Product(BaseModel):
    id = pw.AutoField(column_name="id", primary_key=True)
    company = pw.CharField(column_name="company")
    product_description = pw.CharField(column_name="productdescription")
    price = pw.FloatField(column_name="price")


class ProductSchema(BaseScheme):
    class Meta:
        model = Product

    description = fields.Str(data_key="description")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
