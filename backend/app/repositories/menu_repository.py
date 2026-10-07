from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menu_item import MenuItem


class MenuRepository:

    @staticmethod
    async def get_all(
        session: AsyncSession,
        including_unavailable: bool = False,
    ) -> list[MenuItem]:
        query = select(MenuItem)
        if not including_unavailable:
            query = query.where(MenuItem.is_available.is_(True))

        query = query.order_by(MenuItem.category, MenuItem.name)
        result = await session.execute(query)

        return list(result.scalars().all())

    @staticmethod
    async def get_by_id(
        session: AsyncSession,
        item_id: UUID,
    ) -> MenuItem | None:

        result = await session.execute(select(MenuItem).where(MenuItem.id == item_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def create(
        session: AsyncSession,
        item: MenuItem,
    ) -> MenuItem:

        session.add(item)

        await session.commit()

        await session.refresh(item)

        return item

    @staticmethod
    async def update(
        session: AsyncSession,
        item: MenuItem,
    ) -> MenuItem:

        await session.commit()

        await session.refresh(item)

        return item

    @staticmethod
    async def delete(
        session: AsyncSession,
        item: MenuItem,
    ) -> None:
        await session.delete(item)
        await session.commit()
