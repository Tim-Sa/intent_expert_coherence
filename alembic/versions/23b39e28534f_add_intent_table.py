"""Add intent table

Revision ID: 23b39e28534f
Revises: 20d4fb75df33
Create Date: 2025-02-14 12:44:33.079300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23b39e28534f'
down_revision: Union[str, None] = '20d4fb75df33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.create_table(
        'intent',
        sa.Column('intent_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('expert_id', sa.Integer, sa.ForeignKey('expert.expert_id'), nullable=False),
        sa.Column('name', sa.Text, nullable=True),
        sa.Column('type_id', sa.Integer, nullable=False),
        sa.Column('frequency', sa.Integer, nullable=True),
        sa.Column('k_fleiss_coherence', sa.Numeric(), nullable=True, default=None),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('intent')