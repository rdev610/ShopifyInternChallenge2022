from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15000000000000000))
    category = db.Column(db.String(15000000000000))
    count = db.Column(db.Integer)
    description = db.Column(db.String(100000000000000000000000000000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    products = db.relationship('Product')