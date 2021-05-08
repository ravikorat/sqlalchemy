"""adding image field

Revision ID: 400543a126d7
Revises: bf7154c712f8
Create Date: 2021-05-07 08:40:14.857936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '400543a126d7'
down_revision = 'bf7154c712f8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users",sa.Column('url',sa.String(200)))


def downgrade():
    op.drop_column("users","url")
