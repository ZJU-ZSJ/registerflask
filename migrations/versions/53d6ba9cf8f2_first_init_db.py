"""first init db

Revision ID: 53d6ba9cf8f2
Revises: 
Create Date: 2017-10-21 20:47:10.481370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d6ba9cf8f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('major', sa.Text(), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('studentid', sa.String(length=64), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('question3', sa.Integer(), nullable=True),
    sa.Column('whywants1', sa.Text(), nullable=True),
    sa.Column('question4', sa.Integer(), nullable=True),
    sa.Column('whywants2', sa.Text(), nullable=True),
    sa.Column('intro', sa.Text(), nullable=True),
    sa.Column('why', sa.Text(), nullable=True),
    sa.Column('what', sa.Text(), nullable=True),
    sa.Column('question5', sa.Boolean(), nullable=True),
    sa.Column('day25', sa.Boolean(), nullable=True),
    sa.Column('day26', sa.Boolean(), nullable=True),
    sa.Column('day27', sa.Boolean(), nullable=True),
    sa.Column('day28', sa.Boolean(), nullable=True),
    sa.Column('day291', sa.Boolean(), nullable=True),
    sa.Column('day29', sa.Boolean(), nullable=True),
    sa.Column('day30', sa.Boolean(), nullable=True),
    sa.Column('remarks', sa.String(length=64), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('filename', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('students')
    # ### end Alembic commands ###
