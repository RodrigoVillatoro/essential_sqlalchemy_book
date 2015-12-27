"""Renaming cookies to new_cookies

Revision ID: 31f040577cc
Revises: 294d056d441
Create Date: 2015-12-28 00:17:56.372208

"""

# revision identifiers, used by Alembic.
revision = '31f040577cc'
down_revision = '294d056d441'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.rename_table('cookies', 'new_cookies')


def downgrade():
    op.rename_table('new_cookies', 'cookies')
