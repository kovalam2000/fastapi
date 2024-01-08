"""add content column to post table

Revision ID: ef21b905c5b7
Revises: 00ff9572a32f
Create Date: 2024-01-07 13:39:22.189163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef21b905c5b7'
down_revision: Union[str, None] = '00ff9572a32f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
