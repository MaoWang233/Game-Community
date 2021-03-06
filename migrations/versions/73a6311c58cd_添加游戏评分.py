"""'添加游戏评分'

Revision ID: 73a6311c58cd
Revises: e3d2e6ac7953
Create Date: 2016-06-13 12:54:46.998124

"""

# revision identifiers, used by Alembic.
revision = '73a6311c58cd'
down_revision = 'e3d2e6ac7953'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scores',
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'game_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scores')
    ### end Alembic commands ###
