# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from fm_study import app, db, model


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()