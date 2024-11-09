from app.models.location import Location
from app.exceptions import NotFound
from sqlmodel import Session, select


def get_location_by_id(id: int, session: Session) -> Location:
    location_query = select(Location).where(Location.id == id)
    location = session.exec(location_query).first()

    if location is None:
        raise NotFound(Location, f"No location with {id} found")

    return location
