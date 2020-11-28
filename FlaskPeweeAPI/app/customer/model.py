import peewee as pw
from marshmallow import fields
from marshmallow_peewee import ModelSchema

from app import BaseModel



class Customer(BaseModel):
    id = pw.AutoField(primary_key=True)
    customer_number = pw.CharField(column_name="customernumber", max_length=30)
    firstname = pw.CharField(max_length=100)
    surname = pw.CharField(max_length=100)
    username = pw.CharField(max_length=30)
    dob = pw.DateField()


class Address(BaseModel):
    id = pw.AutoField(primary_key=True)
    customer = pw.ForeignKeyField(Customer,
                                  column_name="customerid",
                                  backref="addresses",
                                  lazy_load=True)
    address_type = pw.CharField(column_name="addresstype")
    address_line_1 = pw.CharField(column_name="addressline1")
    address_line_2 = pw.CharField(column_name="addressline2")
    address_line_3 = pw.CharField(column_name="addressline3")
    state = pw.CharField()
    postcode = pw.CharField()
    country = pw.CharField()


class CustomerSchema(ModelSchema):
    class Meta:
        model = Customer


class CustomerDetailSchema(CustomerSchema):
    addresses = fields.List(fields.Nested("AddressSchema", exclude=["customer"]))


class AddressSchema(ModelSchema):
    class Meta:
        model = Address

    customer = fields.Nested(CustomerDetailSchema(exclude=["addresses"]))


customer_schema = CustomerDetailSchema()
customers_schema = CustomerSchema(many=True)
