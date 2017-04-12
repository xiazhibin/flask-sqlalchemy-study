"""empty message

Revision ID: 3eff5669118f
Revises: c958e0220a50
Create Date: 2017-03-30 15:15:37.010390

"""

# revision identifiers, used by Alembic.
revision = '3eff5669118f'
down_revision = 'c958e0220a50'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('update_at', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'update_at')
    # ### end Alembic commands ###
