from app.api import api
from app.routes.location import router as location_router


def load_routes() -> None:
    api.include_router(location_router)
