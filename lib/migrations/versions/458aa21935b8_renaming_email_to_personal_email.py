"""Renaming email to personal_email

Revision ID: 458aa21935b8
Revises: 6fee1e5d5653
Create Date: 2023-11-01 11:21:51.268084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '458aa21935b8'
down_revision = '6fee1e5d5653'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    # op.alter_column('email', 'personal_email')


def downgrade() -> None:
    pass
    # op.alter_column('personal_email, email')
