"""empty message

Revision ID: 2403a968aed7
Revises: 28ea0bfc74a7
Create Date: 2023-09-06 17:11:46.680101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2403a968aed7'
down_revision = '28ea0bfc74a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('persons_name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('planet_name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('vehicle_name', sa.String(length=50), nullable=False))

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=1000), nullable=True))

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('diameter',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('rotation_period',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('orbital_period',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('gravity',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('population',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('terrain',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=1000),
               existing_nullable=True)

    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_column('description')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=30),
               existing_nullable=True)
        batch_op.alter_column('terrain',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=True)
        batch_op.alter_column('climate',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.alter_column('population',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.alter_column('gravity',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.alter_column('orbital_period',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.alter_column('rotation_period',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.alter_column('diameter',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('description')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_column('vehicle_name')
        batch_op.drop_column('planet_name')
        batch_op.drop_column('persons_name')

    # ### end Alembic commands ###
