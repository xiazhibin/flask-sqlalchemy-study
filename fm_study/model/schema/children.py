from fm_study import db

class Child(db.Model):
    __tablename__ = 'child'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))

    def __repr__(self):
        return "Child(key=%r)" % self.key