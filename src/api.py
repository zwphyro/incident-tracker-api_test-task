from fastapi import APIRouter

from src.incidents.routes import router as incidents_router

router = APIRouter()

router.include_router(incidents_router, prefix="/incidents")
