"""client_name

Revision ID: 2b2fd26809df
Revises: 4e9daa9e85c7
Create Date: 2022-10-28 10:05:37.260985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b2fd26809df'
down_revision = '4e9daa9e85c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('name', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clients', 'name')
    # ### end Alembic commands ###
