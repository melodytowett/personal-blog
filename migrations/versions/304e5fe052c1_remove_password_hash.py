"""remove password hash

Revision ID: 304e5fe052c1
Revises: 72c9dd6567bf
Create Date: 2022-03-12 15:26:08.854932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '304e5fe052c1'
down_revision = '72c9dd6567bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
