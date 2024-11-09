from sqlmodel import Session, select

from app.exceptions import NotFound
from app.models.location import Location


def get_location_by_id(id: int, session: Session) -> Location:
    """
    Lookup location record by ID

    Raises if no location is found
    """
    location_query = select(Location).where(Location.id == id)
    location = session.exec(location_query).first()

    if location is None:
        raise NotFound(Location, f"No location with {id} found")

    return location
