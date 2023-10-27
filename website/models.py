from . import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(9), unique=True)
    first_name = db.Column(db.String(25))
    carrier = db.Column(db.String(25))