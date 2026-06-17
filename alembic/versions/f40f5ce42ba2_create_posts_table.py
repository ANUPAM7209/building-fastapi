"""create posts table

Revision ID: f40f5ce42ba2
Revises: e5cafb3992a7
Create Date: 2026-06-17 22:50:36.861124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f40f5ce42ba2'
down_revision: Union[str, None] = 'e5cafb3992a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
