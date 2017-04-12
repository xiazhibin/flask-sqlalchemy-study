from datetime import datetime
from fm_study import db
from sqlalchemy import CheckConstraint


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    name = db.Column(db.String, index=True)
    price = db.Column(db.Float(10, 2))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', lazy='dynamic')
    update_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    CheckConstraint('price > 0', name='ck_book_price_positive')
