"""empty message

Revision ID: 894c4ad1e760
Revises: 95b9fa751136
Create Date: 2016-08-30 17:43:23.619670

"""

# revision identifiers, used by Alembic.
revision = '894c4ad1e760'
down_revision = '95b9fa751136'

from alembic import op
import sqlalchemy as sa
from hashlib import sha1
import os
from sqlalchemy import Table, MetaData, select


def random_value():
    return sha1(os.urandom(24)).hexdigest()


def upgrade():
    op.add_column('user', sa.Column('token', sa.String(), nullable=True))
    user_table = Table(
        'user', MetaData(),
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('token', sa.String())
    )

    connection = op.get_bind()
    for row in connection.execute(select([user_table.c.id])):
        connection.execute(
            user_table.update().values(token=random_value()).where(user_table.c.id == row['id'])
        )
    op.create_unique_constraint('user_token_key', 'user', ['token'])


def downgrade():
    op.drop_constraint('user_token_key', 'user', type_='unique')
    op.drop_column('user', 'token')
