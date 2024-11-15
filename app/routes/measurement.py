from fastapi import APIRouter, Depends
from sqlmodel import Session, desc, select

from app.db import session_fastapi_dependency
from app.models.measurement import MeasurementResponse, Measurement
from app.services.measurement import get_measurement_by_id

router = APIRouter(prefix="/location/{location_id}/measurement")


@router.get(
    "/",
    response_model=list[MeasurementResponse],
    tags=["Measurement"],
    description="Get latest measurements.",
)
def get_latest_measurements(
    location_id: int,
    session: Session = Depends(session_fastapi_dependency),
) -> list[MeasurementResponse]:
        return [MeasurementResponse.from_data_model(measurement) for measurement in session.exec(
            select(Measurement)
            .where(Measurement.location_id == location_id)
            .order_by(desc(Measurement.date))
            .limit(5)
        ).all()]
    


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
