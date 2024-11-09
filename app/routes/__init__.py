from fastapi import APIRouter

from app.routes.location import router as location_router
from app.routes.measurement import router as measurement_router


def get_routers() -> list[APIRouter]:
    return [location_router, measurement_router]
