"""Add intent type table

Revision ID: 20d4fb75df33
Revises: 30eb4911ec6c
Create Date: 2025-02-14 12:42:08.835945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20d4fb75df33'
down_revision: Union[str, None] = '30eb4911ec6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'intent_type',
        sa.Column('type_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('expert_id', sa.Integer, sa.ForeignKey('expert.expert_id'), nullable=False),
        sa.Column('name', sa.Text, nullable=True),
        sa.Column('frequency', sa.Integer, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('intent_type')