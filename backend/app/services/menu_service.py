from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menu_item import MenuItem
from app.repositories.menu_repository import MenuRepository
from app.schemas.menu import MenuItemCreate, MenuItemUpdate

class MenuService:

    @staticmethod
    async def get_menu(
        session: AsyncSession,
    ):

        return await MenuRepository.get_all(
            session=session,
            # include_unavailable=False,
        )

    @staticmethod
    async def get_menu_item(
        session: AsyncSession,
        item_id: UUID,
    ):


        return await MenuRepository.get_by_id(
            session,
            item_id,
        )

    @staticmethod
    async def create_item(
        session: AsyncSession,
        data: MenuItemCreate,
    ):
        item = MenuItem(
            name=data.name,
            description=data.description,
            base_price=data.base_price,
            category=data.category,
            is_available=data.is_available,
        )

        return await MenuRepository.create(
            session,
            item,                                            
        )
    
    @staticmethod
    async def update_item(
        session:AsyncSession,
        item: MenuItem,
        data: MenuItemUpdate,
    ):
        updates = data.model_dump(
            exclude_unset=True
        )

        for field, value in updates.items():
            setattr(item, field, value)

        return await MenuRepository.update(
            session,
            item,
        )

    @staticmethod
    async def delete_item(
        session: AsyncSession,
        item: MenuItem,
    ):
        await MenuRepository.delete(
            session,
            item,
        )