from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.rbac_test import router as rbac_test_router

from app.core.config import settings
from app.api.routes.menu import router as menu_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for The Fifth Flavor QSR Platform",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(rbac_test_router)
app.include_router(menu_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Fifth Flavor API",
        "version": settings.app_version,
    }
