"""create challenges table

Revision ID: 956913c7a115
Revises: 5f87d88f6e96
Create Date: 2023-04-12 16:20:19.383316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '956913c7a115'
down_revision = '5f87d88f6e96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('challenger_id', sa.Integer(), nullable=True),
    sa.Column('challengee_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['challengee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['challenger_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('challenges')
    # ### end Alembic commands ###