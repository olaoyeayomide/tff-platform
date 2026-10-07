from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import require_role
from app.core.database import get_db
from app.models.menu_item import MenuItem
from app.models.profile import Profile, UserRole
from app.schemas.menu import (
    MenuItemCreate,
    MenuItemResponse,
    MenuItemUpdate,
)
from app.services.menu_service import MenuService

router = APIRouter(
    prefix="/menu",
    tags=["Menu"],
)


@router.get(
    "",
    response_model=list[MenuItemResponse],
)
async def get_menu(
    session: AsyncSession = Depends(get_db),
):
    return await MenuService.get_menu(session)


@router.get(
    "/{item_id}",
    response_model=MenuItemResponse,
)
async def get_menu_item(
    item_id: UUID,
    session: AsyncSession = Depends(get_db),
):
    item = await MenuService.get_menu_item(
        session,
        item_id,
    )

    if not item or not item.is_available:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found",
        )

    return item


@router.post(
    "",
    response_model=MenuItemResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_menu_item(
    data: MenuItemCreate,
    session: AsyncSession = Depends(get_db),
    admin: Profile = Depends(require_role(UserRole.ADMIN)),
):
    return await MenuService.create_item(
        session,
        data,
    )


@router.patch(
    "/{item_id}",
    response_model=MenuItemResponse,
)
async def update_menu_item(
    item_id: UUID,
    data: MenuItemUpdate,
    session: AsyncSession = Depends(get_db),
    admin: Profile = Depends(require_role(UserRole.ADMIN)),
):
    item = await MenuService.get_menu_item(
        session,
        item_id,
    )

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found",
        )

    return await MenuService.update_item(
        session,
        item,
        data,
    )


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_menu_item(
    item_id: UUID,
    session: AsyncSession = Depends(get_db),
    admin: Profile = Depends(require_role(UserRole.ADMIN)),
):
    item = await MenuService.get_menu_item(
        session,
        item_id,
    )

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found",
        )

    await MenuService.delete_item(
        session,
        item,
    )

    return None
