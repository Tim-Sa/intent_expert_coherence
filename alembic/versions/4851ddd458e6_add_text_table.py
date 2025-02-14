"""Add text table

Revision ID: 4851ddd458e6
Revises: a8eac7cd932a
Create Date: 2025-02-14 12:30:30.769186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4851ddd458e6'
down_revision: Union[str, None] = 'a8eac7cd932a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'text',
        sa.Column('text_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('author.author_id'), nullable=False),
        sa.Column('text', sa.Text),
        sa.Column('sentiment', sa.Numeric(precision=3, scale=2), nullable=True, comment='adjusted to -1 to 1 range'),
        sa.Column('answer_to', sa.Integer, sa.ForeignKey('author.author_id'), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('text')