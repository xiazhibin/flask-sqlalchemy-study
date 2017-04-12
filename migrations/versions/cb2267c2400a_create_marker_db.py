"""create marker db

Revision ID: cb2267c2400a
Revises: 894c4ad1e760
Create Date: 2016-09-19 10:10:24.058611

"""

# revision identifiers, used by Alembic.
revision = 'cb2267c2400a'
down_revision = '894c4ad1e760'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marker',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('people')
    op.drop_constraint(u'user_token_key', 'user', type_='unique')
    op.drop_column('user', 'token')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_unique_constraint(u'user_token_key', 'user', ['token'])
    op.create_table('people',
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('followers', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('followees', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('answers', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('agrees', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'people_pkey')
    )
    op.drop_table('marker')
    ### end Alembic commands ###
