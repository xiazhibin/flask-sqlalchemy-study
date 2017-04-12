from fm_study import db
from somemixin import SomeMixin


class Marker(db.Model, SomeMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
