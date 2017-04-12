from fm_study import db


class ProxyDict(object):
    def __init__(self, parent, collection_name, childclass, keyname):
        self.parent = parent
        self.collection_name = collection_name
        self.childclass = childclass
        self.keyname = keyname

    @property
    def collection(self):
        return getattr(self.parent, self.collection_name)

    def keys(self):
        descriptor = getattr(self.childclass, self.keyname)
        return [x[0] for x in self.collection.values(descriptor)]

    def __getitem__(self, key):
        x = self.collection.filter_by(**{self.keyname: key}).first()
        if x:
            return x
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            existing = self[key]
            self.collection.remove(existing)
        except KeyError:
            pass
        self.collection.append(value)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    _collection = db.relationship("Child", lazy="dynamic",
                                  cascade="all, delete-orphan")

    @property
    def child_map(self):
        from .children import Child
        return ProxyDict(self, '_collection', Child, 'key')
