from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.health import router as health_router
from app.core.config import settings

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


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Fifth Flavor API",
        "version": settings.app_version,
    }
