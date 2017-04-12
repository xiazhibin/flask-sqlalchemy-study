from fm_study import db
from datetime import datetime


class SomeMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.now)