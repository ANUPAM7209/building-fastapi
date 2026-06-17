"""add user table

Revision ID: f397b54d45c1
Revises: 283f6588b5a6
Create Date: 2026-06-17 23:08:57.592673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f397b54d45c1'
down_revision: Union[str, None] = '283f6588b5a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:    
    pass


def downgrade() -> None:
    pass
