from datetime import datetime
from sqlalchemy import text
from fm_study import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    content = db.Column(db.String)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    commenter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    commenter = db.relationship('User', lazy='joined', uselist=False)
