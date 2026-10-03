from datetime import datetime
from enum import Enum
from uuid import UUID
from sqlalchemy import DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserRole(str, Enum):
    CUSTOMER = "CUSTOMER"
    KITCHEN_STAFF = "KITCHEN_STAFF"


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
    )

    full_name: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    role: Mapped[UserRole] = mapped_column(
        nullable=False,
        default=UserRole.CUSTOMER,
    )

    access_pin_hash: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
