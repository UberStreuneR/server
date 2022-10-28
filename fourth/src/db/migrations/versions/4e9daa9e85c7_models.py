"""models

Revision ID: 4e9daa9e85c7
Revises: 
Create Date: 2022-10-28 09:54:30.913047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e9daa9e85c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('client_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_table('lines',
    sa.Column('line_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('line_id')
    )
    op.create_table('accounts',
    sa.Column('account_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], ),
    sa.PrimaryKeyConstraint('account_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    op.drop_table('lines')
    op.drop_table('clients')
    # ### end Alembic commands ###