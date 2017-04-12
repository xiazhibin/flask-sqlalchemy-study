"""empty message

Revision ID: 826f6c037ba0
Revises: d6a47e98705b
Create Date: 2016-08-30 17:43:23.619670

"""

# revision identifiers, used by Alembic.
revision = '826f6c037ba0'
down_revision = 'd6a47e98705b'

from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Table, MetaData

book_table = Table(
    'book', MetaData(),
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('name', sa.String()),
    sa.Column('created_at', sa.DateTime())
)


def upgrade():
    connection = op.get_bind()
    rv = connection.execute(
        book_table.select().where(book_table.c.name == 'book4')
    )
    if rv is None or rv.rowcount == 0:
        t = connection.execute(
            book_table.insert().values(name='book4', created_at=datetime.now())
        )
        print t.rowcount
        print t.returns_rows


def downgrade():
    connection = op.get_bind()
    connection.execute(
        book_table.delete().where(book_table.c.name == 'book4')
    )
