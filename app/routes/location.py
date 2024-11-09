from fastapi import APIRouter
from sqlmodel import select

from app.db import session
from app.models.location import Location

router = APIRouter(prefix="/location")


@router.get("/")
def search_location() -> list[Location]:
    with session() as db:
        locations = select(Location)
        return db.exec(locations).all()


@router.get("/{id}")
def get_location(id: int) -> Location:
    with session() as db:
        location_query = select(Location).where(Location.id == id)
        return db.exec(location_query).first()
