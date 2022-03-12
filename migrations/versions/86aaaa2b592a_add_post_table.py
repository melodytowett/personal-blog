"""add post table

Revision ID: 86aaaa2b592a
Revises: 3f82f1c2635b
Create Date: 2022-03-12 11:53:58.751254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86aaaa2b592a'
down_revision = '3f82f1c2635b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('post_title', sa.String(), nullable=True),
    sa.Column('post_blog', sa.String(), nullable=True),
    sa.Column('time_posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###