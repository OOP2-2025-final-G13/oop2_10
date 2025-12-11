from peewee import Model, ForeignKeyField, DateTimeField, IntegerField
from .db import db
from .user import User
from .product import Product

class Order(Model):
    user = ForeignKeyField(User, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    quantity = IntegerField()
    order_date = DateTimeField()

    class Meta:
        database = db
