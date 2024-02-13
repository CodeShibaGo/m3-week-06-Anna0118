"""add post table

Revision ID: 778c383432b2
Revises: 77b1d7cddf46
Create Date: 2024-02-13 13:57:06.771625

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '778c383432b2'
down_revision = '77b1d7cddf46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=256),
               type_=sa.String(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))

    op.drop_table('post')
    # ### end Alembic commands ###
