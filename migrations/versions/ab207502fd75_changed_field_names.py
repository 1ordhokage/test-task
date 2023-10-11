"""changed field names

Revision ID: ab207502fd75
Revises: 94d5cb2ee428
Create Date: 2023-10-10 23:14:11.701975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab207502fd75'
down_revision: Union[str, None] = '94d5cb2ee428'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('question', sa.String(), nullable=False))
    op.add_column('question', sa.Column('answer', sa.String(), nullable=False))
    op.drop_column('question', 'answer_text')
    op.drop_column('question', 'question_text')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('question_text', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('question', sa.Column('answer_text', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('question', 'answer')
    op.drop_column('question', 'question')
    # ### end Alembic commands ###