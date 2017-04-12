"""empty message

Revision ID: 265f2fbff29e
Revises: 1e2f974bbe49
Create Date: 2017-02-23 18:10:21.590624

"""

# revision identifiers, used by Alembic.
revision = '265f2fbff29e'
down_revision = '1e2f974bbe49'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('commenter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['commenter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###