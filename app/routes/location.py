from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db import session_fastapi_dependency
from app.models.location import Location, LocationPartial
from app.services.location import get_location_by_id

router = APIRouter(prefix="/location")


@router.get(
    "/",
    response_model=list[Location],
    tags=["Location"],
    description="Search for locations by wildcard string.",
)
def search_location(
    search: str,
    session: Session = Depends(session_fastapi_dependency),
) -> list[Location]:
    if len(search) < 3:
        return []

    locations = select(Location).where(Location.city.ilike(f"%{search}%"))  # type: ignore[attr-defined]

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
    location_partial: LocationPartial,
    session: Session = Depends(session_fastapi_dependency),
) -> Location:
    # Ignore types here, the validator will catch these
    location = Location(
        city=location_partial.city,  # type: ignore[arg-type]
        state=location_partial.state,  # type: ignore[arg-type]
        country=location_partial.country,  # type: ignore[arg-type]
        lat=location_partial.lat,  # type: ignore[arg-type]
        long=location_partial.long,  # type: ignore[arg-type]
    )
    location.model_validate(location)

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
    id: int,
    location_partial: LocationPartial,
    session: Session = Depends(session_fastapi_dependency),
) -> Location:
    location = get_location_by_id(id, session)

    if location_partial.city is not None:
        location.city = location_partial.city

    if location_partial.state is not None:
        location.state = location_partial.state

    if location_partial.country is not None:
        location.state = location_partial.country

    if location_partial.lat is not None:
        location.lat = location_partial.lat

    if location_partial.long is not None:
        location.long = location_partial.long

    session.commit()
    session.refresh(location)

    return location


@router.delete(
    "/{id}",
    status_code=204,
    tags=["Location"],
    description="Delete an existing location.",
)
def delete_location(
    id: int,
    session: Session = Depends(session_fastapi_dependency),
) -> None:
    location = get_location_by_id(id, session)

    session.delete(location)
    session.commit()

    return None
