from fastapi import APIRouter, Depends

from app.core.auth import require_role
from app.models.profile import Profile, UserRole

router = APIRouter(
    prefix="/rbac-test",
    tags=["RBAC Test"],
)


@router.get("/customer")
async def customer_only(
    profile: Profile = Depends(require_role(UserRole.CUSTOMER)),
):
    return {
        "message": "Customer access granted",
        "user_id": str(profile.id),
        "role": profile.role,
    }


@router.get("/kitchen")
async def kitchen_only(
    profile: Profile = Depends(require_role(UserRole.KITCHEN_STAFF)),
):
    return {
        "message": "Kitchen access granted",
        "user_id": str(profile.id),
        "role": profile.role,
    }


@router.get("/admin")
async def admin_only(
    profile: Profile = Depends(require_role(UserRole.ADMIN)),
):
    return {
        "message": "Admin access granted",
        "user_id": str(profile.id),
        "role": profile.role,
    }
