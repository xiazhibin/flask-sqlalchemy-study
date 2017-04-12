from datetime import datetime
from sqlalchemy import text
from fm_study import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    login = db.Column(db.String, unique=True)
    nickname = db.Column(db.String)
    books = db.relationship('Book', backref='user', lazy='dynamic', order_by="desc(Book.created_at)")
