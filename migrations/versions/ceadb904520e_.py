"""empty message

Revision ID: ceadb904520e
Revises: e0033cc40aeb
Create Date: 2023-09-13 18:35:15.449171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceadb904520e'
down_revision = 'e0033cc40aeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vehicle_id', sa.Integer(), nullable=True))
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_foreign_key(None, 'vehicles', ['vehicle_id'], ['id'])
        batch_op.drop_column('persons_name')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint('people_favorites_id_fkey', type_='foreignkey')
        batch_op.drop_column('favorites_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorites_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('people_favorites_id_fkey', 'favorites', ['favorites_id'], ['id'])

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('persons_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('vehicle_id')

    # ### end Alembic commands ###
