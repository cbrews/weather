from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select


from app.db import session_fastapi_dependency
from app.models.location import Location

router = APIRouter(prefix="/location")


@router.get(
    "/", response_model=list[Location], tags=["Location"], description="Search for locations by wildcard string."
)
def search_location(
    name: str = Query(), session: Session = Depends(session_fastapi_dependency),
) -> list[Location]:
    locations = select(Location).where(Location.name == name)
    return list(session.exec(locations).all())


@router.get("/{id}", response_model=Location, tags=["Location"], description="Get a location by ID.")
def get_location(
    id: int, session: Session = Depends(session_fastapi_dependency),
) -> Location:
    location_query = select(Location).where(Location.id == id)
    location = session.exec(location_query).first()

    if location is None:
        raise HTTPException(status_code=404, detail=f"No location with {id} found")

    return location

@router.post("/", response_model=Location, tags=["Location"], description="Create a new location.")
def create_location(location: Location, session: Session = Depends(session_fastapi_dependency)):
    location.id = None
    session.add(location)
    session.commit()

    session.refresh(location)

    return location