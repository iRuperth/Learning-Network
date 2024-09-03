"""empty message

Revision ID: 290ed54c4585
Revises: 499fe2c2a0a8
Create Date: 2024-09-03 08:37:37.971809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290ed54c4585'
down_revision = '499fe2c2a0a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.alter_column('portada',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('nivel',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('precio',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('fecha_inicio',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.alter_column('fecha_inicio',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('precio',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('nivel',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('portada',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    # ### end Alembic commands ###
