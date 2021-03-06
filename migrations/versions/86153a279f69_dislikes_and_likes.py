"""dislikes and likes

Revision ID: 86153a279f69
Revises: c3037cbcc7a0
Create Date: 2019-07-02 16:18:48.958167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86153a279f69'
down_revision = 'c3037cbcc7a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('dislikes', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'likes')
    op.drop_column('pitches', 'dislikes')
    # ### end Alembic commands ###
