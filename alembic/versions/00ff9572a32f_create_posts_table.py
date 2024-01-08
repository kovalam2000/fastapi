"""create posts table

Revision ID: 00ff9572a32f
Revises: 
Create Date: 2024-01-07 12:35:39.747218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00ff9572a32f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True)
                    , sa.Column('title', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
