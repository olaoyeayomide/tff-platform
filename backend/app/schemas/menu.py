from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MenuItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str | None = None
    base_price: Decimal = Field(gt=0)
    category: str = Field(min_length=1, max_length=100)
    is_available: bool = True


class MenuItemUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )
    description: str | None = None
    base_price: Decimal | None = Field(
        default=None,
        gt=0,
    )
    category: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    is_available: bool | None = None


class MenuItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None
    base_price: Decimal
    category: str
    is_available: bool
    created_at: datetime
