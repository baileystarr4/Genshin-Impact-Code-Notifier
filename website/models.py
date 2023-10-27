from . import db
from sqlalchemy.sql import func


class User(db.Model):
    phone_number = db.Column(db.String(9), primary_key=True)
    first_name = db.Column(db.String(25))
    carrier = db.Column(db.String(25))