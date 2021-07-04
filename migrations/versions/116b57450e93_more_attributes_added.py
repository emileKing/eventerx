"""more attributes added

Revision ID: 116b57450e93
Revises: 
Create Date: 2021-07-02 10:51:06.319710

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '116b57450e93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('school_institution', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.add_column('task', sa.Column('priority', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('description', sa.String(length=256), nullable=False))
    op.add_column('task', sa.Column('taskstate_id', sa.String(length=50), nullable=False))
    op.create_foreign_key(None, 'task', 'task_state', ['taskstate_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'taskstate_id')
    op.drop_column('task', 'description')
    op.drop_column('task', 'priority')
    op.alter_column('school_institution', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_table('task_state')
    # ### end Alembic commands ###