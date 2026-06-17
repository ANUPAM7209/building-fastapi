"""add content column to posts table

Revision ID: 283f6588b5a6
Revises: f40f5ce42ba2
Create Date: 2026-06-17 23:01:17.887660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '283f6588b5a6'
down_revision: Union[str, None] = 'f40f5ce42ba2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('email', sa.String(), nullable=False, unique=True),
                sa.Column('password', sa.String(), nullable=False),
                sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email')

                )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
