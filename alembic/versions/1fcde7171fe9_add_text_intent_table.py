"""Add text intent table

Revision ID: 1fcde7171fe9
Revises: 23b39e28534f
Create Date: 2025-02-14 12:48:13.472738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fcde7171fe9'
down_revision: Union[str, None] = '23b39e28534f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(
        'text_intent',
        sa.Column('text_intent_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('text_id', sa.Integer, sa.ForeignKey('text.text_id'), nullable=False),
        sa.Column('expert_id', sa.Integer, sa.ForeignKey('expert.expert_id'), nullable=False),
        sa.Column('intent_id', sa.Integer, sa.ForeignKey('intent.intent_id'), nullable=False),
        sa.Column('is_true', sa.Boolean, nullable=False, default=True),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('text_intent')