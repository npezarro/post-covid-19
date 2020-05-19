"""empty message

Revision ID: 0c53f2984325
Revises: 168048b91b28
Create Date: 2020-05-19 09:16:17.910512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c53f2984325'
down_revision = '168048b91b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_guess', sa.Date(), nullable=True))
    op.create_index(op.f('ix_post_date_guess'), 'post', ['date_guess'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_date_guess'), table_name='post')
    op.drop_column('post', 'date_guess')
    # ### end Alembic commands ###
