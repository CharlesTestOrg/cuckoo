# Copyright (C) 2010-2014 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

"""add task owner

Revision ID: 3aa42d870199
Revises: 18eee46c6f81
Create Date: 2014-12-04 11:19:49.388410

"""

# revision identifiers, used by Alembic.
revision = '3aa42d870199'
down_revision = '18eee46c6f81'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('tasks', sa.Column('owner', sa.String(length=64), nullable=True))


def downgrade():
    op.drop_column('tasks', 'owner')
