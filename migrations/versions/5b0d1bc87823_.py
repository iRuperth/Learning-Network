"""empty message

Revision ID: 5b0d1bc87823
Revises: 043c5b23ab84
Create Date: 2024-09-02 10:50:24.334975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b0d1bc87823'
down_revision = '043c5b23ab84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pagos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curso_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'curso', ['curso_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pagos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('curso_id')

    # ### end Alembic commands ###
