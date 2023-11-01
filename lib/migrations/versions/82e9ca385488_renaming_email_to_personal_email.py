"""Renaming email to personal_email

Revision ID: 82e9ca385488
Revises: 458aa21935b8
Create Date: 2023-11-01 11:34:37.142544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82e9ca385488'
down_revision = '458aa21935b8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'email', new_column_name='personal_email')


def downgrade() -> None:
    op.alter_column('scholars', 'personal_email', new_column_name='email')
