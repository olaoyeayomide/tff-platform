from fastapi import APIRouter, Depends
from app.core.auth import get_current_profile
from app.models.profile import Profile
from app.schemas.auth import ProfileResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get(
    "/me",
    response_model=ProfileResponse,
)
async def get_me(
    profile: Profile = Depends(get_current_profile),
):

    return profile
