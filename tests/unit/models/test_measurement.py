from datetime import date

import pytest

from app.models.measurement import Measurement, MeasurementResponse
from app.util import celcius_to_fahrenheit


@pytest.fixture
def measurement_fixture() -> Measurement:
    return Measurement(
        id=1,
        location_id=1,
        date=date(2024, 1, 1),
        temp_high=28,
        temp_low=20,
        temp_avg=24,
    )


def test_measurement_from_orm(measurement_fixture: Measurement) -> None:
    measurement_response = MeasurementResponse.from_data_model(measurement_fixture)

    assert measurement_response is not None
    assert measurement_response.id == measurement_fixture.id
    assert measurement_response.date == measurement_fixture.date
    assert measurement_response.temp_high.celcius == measurement_fixture.temp_high
    assert measurement_response.temp_high.fahrenheit == celcius_to_fahrenheit(
        measurement_fixture.temp_high
    )
    assert measurement_response.temp_low.celcius == measurement_fixture.temp_low
    assert measurement_response.temp_low.fahrenheit == celcius_to_fahrenheit(
        measurement_fixture.temp_low
    )
    assert measurement_response.temp_avg.celcius == measurement_fixture.temp_avg
    assert measurement_response.temp_avg.fahrenheit == celcius_to_fahrenheit(
        measurement_fixture.temp_avg
    )


def test_measurement_from_orm__unsaved(measurement_fixture: Measurement) -> None:
    measurement_fixture.id = None  # Simulate unsaved measurement fixture

    with pytest.raises(ValueError):
        MeasurementResponse.from_data_model(measurement_fixture)
