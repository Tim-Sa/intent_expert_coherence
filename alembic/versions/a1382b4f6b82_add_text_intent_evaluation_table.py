"""Add text intent evaluation table

Revision ID: a1382b4f6b82
Revises: 1fcde7171fe9
Create Date: 2025-02-14 13:01:29.736950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1382b4f6b82'
down_revision: Union[str, None] = '1fcde7171fe9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(
        'text_intent_ev',
        sa.Column('text_intent_ev_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('text_intent_id', sa.Integer, sa.ForeignKey('text_intent.text_intent_id'), nullable=False),
        sa.Column('expert_id', sa.Integer, sa.ForeignKey('expert.expert_id'), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('evaluation', sa.Boolean, nullable=True, default=None, comment="agree/disagree with intent in text")
    )


def downgrade():
    op.drop_table('text_intent_ev')