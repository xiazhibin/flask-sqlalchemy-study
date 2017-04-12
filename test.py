from fm_study.model.schema.user import User
from fm_study.model.schema.comment import Comment
from fm_study.model.schema.book import Book
from fm_study.model.schema.parent import Parent
from fm_study.model.schema.children import Child
from fm_study import db
from sqlalchemy.orm import load_only
import datetime

# user = User.query.filter_by(id=1).first()
# user.nickname = 'heheta'
# user.token = 'dadahe'
# db.session.commit()
# print user.nickname
#
# schema = User.query.options(load_only('nickname', 'id')).filter_by(nickname='heheta').first()
# print schema.id

# book = Book.query.filter_by(id=2).first()
# for c in book.comments:
#     print c.content

# c = Comment.query.filter_by(id=2).first()
# print c.content
# print c.commenter.id


b = Book()
b.name = 'bookx'
b.price = -1
db.session.add(b)
db.session.commit()



