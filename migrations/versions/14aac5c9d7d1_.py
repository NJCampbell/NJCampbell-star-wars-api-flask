"""empty message

Revision ID: 14aac5c9d7d1
Revises: b77b9bdf4e07
Create Date: 2023-09-03 22:28:14.084570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14aac5c9d7d1'
down_revision = 'b77b9bdf4e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user__favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('vehicle_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planets', ['planet_id'], ['id'])
        batch_op.create_foreign_key(None, 'vehicles', ['vehicle_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehicle_id')
        batch_op.drop_column('planet_id')

    op.drop_table('user__favorites')
    # ### end Alembic commands ###
