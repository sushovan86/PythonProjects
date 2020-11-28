import logging

import peewee as pw
from flask import Flask
from flask_marshmallow import Marshmallow

from config import *

application = Flask(__name__)
application.config.from_object('config')

ma = Marshmallow(application)
db = pw.PostgresqlDatabase(DATABASE_USERNAME,
                           host=DATABASE_HOST,
                           user=DATABASE_USERNAME,
                           password=DATABASE_PASSWORD)

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class BaseModel(pw.Model):
    class Meta:
        database = db


from app.register_urls import register

register(application)
