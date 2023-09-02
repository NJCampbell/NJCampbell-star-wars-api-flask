"""empty message

Revision ID: 4e73a57a5181
Revises: a7a98ca78a93
Create Date: 2023-09-02 00:36:56.655171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e73a57a5181'
down_revision = 'a7a98ca78a93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('vehicle_class', sa.String(length=50), nullable=True),
    sa.Column('manufacturer', sa.String(length=50), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=50), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('crew', sa.String(length=50), nullable=True),
    sa.Column('passengers', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###
