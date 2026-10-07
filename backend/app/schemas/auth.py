from uuid import UUID

from pydantic import BaseModel, ConfigDict
from app.models.profile import UserRole


class ProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    full_name: str
    phone_number: str | None
    role: UserRole
