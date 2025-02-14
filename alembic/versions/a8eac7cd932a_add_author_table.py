"""Add author table

Revision ID: a8eac7cd932a
Revises: 
Create Date: 2025-02-13 16:37:28.353168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8eac7cd932a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the table with automatic handling of timestamps
    op.create_table(
        'author',
        sa.Column('author_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('nickname', sa.Text(), nullable=True),
        sa.Column('n_texts', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    # Drop the table
    op.drop_table('author')
