from functools import lru_cache
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import create_client, Client

from app.core.config import settings
from app.core.database import AsyncSessionLocal
from app.models.profile import Profile, UserRole

security = HTTPBearer()


@lru_cache
def get_supabase_client() -> Client:
    return create_client(
        settings.supabase_url,
        settings.supabase_publishable_key,
    )


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    try:
        response = get_supabase_client().auth.get_user(token)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
        )

    if not response or not response.user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )
    return response.user


async def get_current_profile(
    user=Depends(get_current_user),
):

    async with AsyncSessionLocal() as session:
        profile = await session.get(Profile, UUID(user.id))

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Profile not found",
        )

    return profile


def require_role(*allowed_roles: UserRole):
    async def role_dependency(
        profile: Profile = Depends(get_current_profile),
    ):
        if profile.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )

        return profile

    return role_dependency
