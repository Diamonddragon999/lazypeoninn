from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    user_code = db.Column(db.Text, unique=True, nullable=False)
    
class Chef(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_code = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    motto = db.Column(db.String(255), unique=True, nullable=False)
    speciality = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.String(255), unique=True, nullable=False)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.String(255), unique=True, nullable=False)

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    path = db.Column(db.String(255), unique=True, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey("user.id"))
    review_title = db.Column(db.String(255), nullable=False)
    review_text = db.Column(db.TEXT, nullable=False)
    review_code = db.Column(db.String(255), unique=True, nullable=False)
