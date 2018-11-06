"""Remove boolean server defaults for migrations

Revision ID: ca61ed4a75fd
Revises: dd1bcd34b36d
Create Date: 2018-11-06 23:32:38.786692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca61ed4a75fd'
down_revision = 'dd1bcd34b36d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('change', 'reverted',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('chat', 'choosing_language',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('chat', 'fix_single_sticker',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('chat', 'is_ban',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('chat', 'is_maintenance',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('chat', 'is_newsfeed',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('chat', 'tagging_random_sticker',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('sticker_set', 'banned',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('sticker_set', 'completely_tagged',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('sticker_set', 'deleted',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('sticker_set', 'furry',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('sticker_set', 'newsfeed_sent',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('sticker_set', 'nsfw',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('tag', 'emoji',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('task', 'reviewed',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('user', 'admin',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('user', 'authorized',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('user', 'reverted',
                    existing_type=sa.BOOLEAN(),
                    server_default=None,
                    existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'reverted',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('user', 'authorized',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('user', 'admin',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('task', 'reviewed',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('tag', 'emoji',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('sticker_set', 'nsfw',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('sticker_set', 'newsfeed_sent',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('sticker_set', 'furry',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('sticker_set', 'deleted',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('sticker_set', 'completely_tagged',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('sticker_set', 'banned',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('chat', 'tagging_random_sticker',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('chat', 'is_newsfeed',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('chat', 'is_maintenance',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('chat', 'is_ban',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('chat', 'fix_single_sticker',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('chat', 'choosing_language',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    op.alter_column('change', 'reverted',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('false'),
                    existing_nullable=False)
    # ### end Alembic commands ###