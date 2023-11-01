"""Renaming students to scholars

Revision ID: 2fdf103bcfe5
Revises: 791279dd0760
Create Date: 2023-11-01 10:52:50.679708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fdf103bcfe5'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
