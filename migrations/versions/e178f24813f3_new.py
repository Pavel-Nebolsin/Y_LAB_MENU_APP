"""new

Revision ID: e178f24813f3
Revises: 
Create Date: 2023-07-28 16:24:26.858698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e178f24813f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_menu_id'), 'menu', ['id'], unique=False)
    op.create_table('submenu',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('menu_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_submenu_id'), 'submenu', ['id'], unique=False)
    op.create_table('dish',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('submenu_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['submenu_id'], ['submenu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_dish_id'), 'dish', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dish_id'), table_name='dish')
    op.drop_table('dish')
    op.drop_index(op.f('ix_submenu_id'), table_name='submenu')
    op.drop_table('submenu')
    op.drop_index(op.f('ix_menu_id'), table_name='menu')
    op.drop_table('menu')
    # ### end Alembic commands ###
