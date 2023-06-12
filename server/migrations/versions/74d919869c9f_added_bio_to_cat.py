"""added bio to cat

Revision ID: 74d919869c9f
Revises: 862aeaef2302
Create Date: 2023-06-12 11:54:56.207623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74d919869c9f'
down_revision = '862aeaef2302'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cats', schema=None) as batch_op:
        batch_op.drop_column('bio')

    # ### end Alembic commands ###