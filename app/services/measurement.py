from sqlmodel import Session, select

from app.exceptions import NotFound
from app.models.measurement import Measurement


def get_measurement_by_id(
    location_id: int, measurement_id: int, session: Session
) -> Measurement:
    """
    Lookup measurement record by ID

    Raises if no measurement is found
    """
    measurement_query = select(Measurement).where(
        Measurement.location_id == location_id, Measurement.id == measurement_id
    )
    measurement = session.exec(measurement_query).first()

    if measurement is None:
        raise NotFound(
            Measurement,
            f"No measurement with {measurement_id} found in location {location_id}",
        )

    return measurement
