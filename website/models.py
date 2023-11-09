from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class MovieCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(10000))
    #Soring a list might not work, Double Check if errors. Could try db.Column(db.ARRAY(db.String(20)))
    genre = db.Column(db.ARRAY(db.String(20)))
    rating = db.Column(db.Float)