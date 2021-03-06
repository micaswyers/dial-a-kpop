"""empty message

Revision ID: 872a01606d43
Revises: 
Create Date: 2019-01-18 14:08:51.198817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872a01606d43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('artist', sa.String(), nullable=True),
    sa.Column('video_url', sa.String(), nullable=False),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_last_played', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs')
    # ### end Alembic commands ###
