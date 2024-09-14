"""Suppression des tables obsolètes

Revision ID: 47fd9c7901c9
Revises: 848d7515a4b2
Create Date: 2024-09-14 13:33:47.042544

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '47fd9c7901c9'
down_revision = '848d7515a4b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    op.drop_table('matches')
    op.drop_table('job_postings')
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('companies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('company_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('company_video', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('company_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=True)

    op.create_table('job_postings',
    sa.Column('posting_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('company_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=False),
    sa.Column('video_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('type', mysql.ENUM('internship', 'job', 'project'), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.company_id'], name='job_postings_ibfk_1'),
    sa.PrimaryKeyConstraint('posting_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('matches',
    sa.Column('match_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('posting_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', mysql.ENUM('pending', 'accepted', 'rejected'), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['posting_id'], ['job_postings.posting_id'], name='matches_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='matches_ibfk_2'),
    sa.PrimaryKeyConstraint('match_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('messages',
    sa.Column('message_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('match_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sender_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('message_text', mysql.TEXT(), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['match_id'], ['matches.match_id'], name='messages_ibfk_1'),
    sa.ForeignKeyConstraint(['sender_id'], ['users.user_id'], name='messages_ibfk_2'),
    sa.PrimaryKeyConstraint('message_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
