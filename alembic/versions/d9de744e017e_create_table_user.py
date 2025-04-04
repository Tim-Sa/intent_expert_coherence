"""create table user

Revision ID: d9de744e017e
Revises: a1382b4f6b82
Create Date: 2025-04-03 12:04:27.360403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9de744e017e'
down_revision: Union[str, None] = 'a1382b4f6b82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(

        'user',

        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(length=20), nullable=False, unique=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('user')