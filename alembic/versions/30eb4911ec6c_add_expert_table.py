"""Add expert table

Revision ID: 30eb4911ec6c
Revises: 4851ddd458e6
Create Date: 2025-02-14 12:35:01.847564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30eb4911ec6c'
down_revision: Union[str, None] = '4851ddd458e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(

        'expert',

        sa.Column('expert_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.Text, nullable=True),
        sa.Column('phone', sa.Text, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('expert')
