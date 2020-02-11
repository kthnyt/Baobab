"""empty message

Revision ID: b6a2a69fbb13
Revises: d8d17ed47c53
Create Date: 2020-02-07 20:21:09.862107

"""

# revision identifiers, used by Alembic.
revision = 'b6a2a69fbb13'
down_revision = 'd8d17ed47c53'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reference', 'uploaded_document',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.drop_column('reference_request', 'reference_submitted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reference_request', sa.Column('reference_submitted', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('reference', 'uploaded_document',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###
