from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from app.services.location import get_location_by_id
from app.db import session_fastapi_dependency
from app.models.location import Location, LocationPartial


router = APIRouter(prefix="/location")


@router.get(
    "/",
    response_model=list[Location],
    tags=["Location"],
    description="Search for locations by wildcard string.",
)
def search_location(
    name: str = Query(),
    session: Session = Depends(session_fastapi_dependency),
) -> list[Location]:
    locations = select(Location).where(Location.name == name)
    return list(session.exec(locations).all())


@router.get(
    "/{id}",
    response_model=Location,
    tags=["Location"],
    description="Get a location by ID.",
)
def get_location(
    id: int,
    session: Session = Depends(session_fastapi_dependency),
) -> Location:

    return get_location_by_id(id, session)


@router.post(
    "/",
    response_model=Location,
    tags=["Location"],
    description="Create a new location.",
)
def create_location(
    location_partial: LocationPartial, session: Session = Depends(session_fastapi_dependency)
) -> Location:
    location = Location(
        name=location_partial.name,
        lat=location_partial.lat,
        long=location_partial.long,
    )

    session.add(location)

    session.commit()
    session.refresh(location)

    return location


@router.put(
    "/{id}",
    response_model=Location,
    tags=["Location"],
    description="Update an existing location.",
)
def update_location(
    id: int, location_partial: LocationPartial, session: Session = Depends(session_fastapi_dependency)
) -> Location:
    location = get_location_by_id(id, session)

    if location_partial.name is not None:
        location.name = location_partial.name

    if location_partial.lat is not None:
        location.lat = location_partial.lat

    if location_partial.long is not None:
        location.long = location_partial.long

    session.commit()
    session.refresh(location)

    return location
