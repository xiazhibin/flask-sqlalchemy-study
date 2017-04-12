"""empty message

Revision ID: 5fc75ef1446f
Revises: 826f6c037ba0
Create Date: 2016-08-30 17:43:23.619670

"""

# revision identifiers, used by Alembic.
revision = '5fc75ef1446f'
down_revision = '826f6c037ba0'

from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Table, MetaData, select

book_table = Table(
    'book', MetaData(),
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('user_id', sa.Integer()),
    sa.Column('name', sa.String())
)

user_table = Table(
    'user', MetaData(),
    sa.Column('id', sa.Integer(), primary_key=True)
)


def upgrade():
    connection = op.get_bind()
    for user_row in connection.execute(user_table.select()):
        for book_row in connection.execute(book_table.select().where(book_table.c.user_id==user_row['id'])):
            print book_row['name']


def downgrade():
    pass
