"""empty message

Revision ID: a5879be2fd07
Revises: d5f87144251f
Create Date: 2019-06-03 15:29:01.144838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5879be2fd07'
down_revision = 'd5f87144251f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cloud_connection',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('bucket', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('access_key_id', sa.String(), nullable=True),
    sa.Column('access_key_secret', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cloud_connection')
    # ### end Alembic commands ###
