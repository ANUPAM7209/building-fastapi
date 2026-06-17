"""add foregin key to posts table

Revision ID: b91b530351fd
Revises: f397b54d45c1
Create Date: 2026-06-18 00:39:48.380798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b91b530351fd'
down_revision: Union[str, None] = 'f397b54d45c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_id_fkey', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_id_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
