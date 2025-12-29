"""create initial user

Revision ID: c866cc593a75
Revises: 
Create Date: 2025-12-29 16:19:06.008734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.core.security import hash_password


# revision identifiers, used by Alembic.
revision: str = 'c866cc593a75'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

''' USUARIO INICIAL
el usuario se crea automáticamente mientras las migración se ejecute
'''
def upgrade() -> None:
    users_table = sa.table(
        "users",
        sa.Column("id", sa.Integer),
        sa.Column("username",sa.String),
        sa.Column("email", sa.String),
        sa.Column("password", sa.String),
        sa.Column("is_active", sa.Boolean)
    )
    
    op.bulk_insert(
        users_table,
        [
            {
                "username": "admin",
                "email": "admin@example.com",
                "password": hash_password("admin123"),
                "is_active": True,
            }
        ]
    )


def downgrade() -> None:
    op.execute("DELETE FROM users WHERE username='admin'")
