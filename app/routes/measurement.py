from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db import session_fastapi_dependency
from app.models.measurement import Measurement
from app.services.measurement import get_measurement_by_id

router = APIRouter(prefix="/location/{location_id}/measurement")


@router.get(
    "/{measurement_id}",
    response_model=Measurement,
    tags=["Measurement"],
    description="Get measurement by ID.",
)
def get_measurement_by_day(
    location_id: int,
    measurement_id: int,
    session: Session = Depends(session_fastapi_dependency),
) -> Measurement:
    return get_measurement_by_id(location_id, measurement_id, session)
