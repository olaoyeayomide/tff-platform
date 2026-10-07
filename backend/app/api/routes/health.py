from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.database import get_db

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def helth_check():
    return {
        "status": "ok",
        "service": "tff-api",
    }


@router.get("/db")
async def database_health_check(
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(text("SELECT 1"))
    return {
        "status": "ok",
        "service": "tff-api",
        "database": result.scalar(),
    }
