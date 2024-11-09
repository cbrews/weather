from datetime import date

from sqlmodel import Field, Relationship, SQLModel

from app.models.location import Location
from app.models.temperature import Temperature
from app.util import celcius_to_fahrenheit


class Measurement(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    location_id: int = Field(foreign_key="location.id")
    date: date
    temp_high: float = Field(description="Stored in celcius")
    temp_low: float = Field(description="Stored in celcius")
    temp_avg: float = Field(description="Stored in celcius")

    location: Location = Relationship(back_populates="measurements")


class MeasurementResponse(SQLModel):
    id: int
    date: date
    temp_high: Temperature
    temp_low: Temperature
    temp_avg: Temperature

    @classmethod
    def from_data_model(cls, orm: Measurement) -> "MeasurementResponse":
        if orm.id is None:
            raise ValueError(
                "Trying to instantiate MeasurementResponse from an unsaved Measurement "
                "object. Make sure the object has been refreshed from the database!"
            )

        return MeasurementResponse(
            id=orm.id,
            date=orm.date,
            temp_high=Temperature(
                celcius=orm.temp_high, fahrenheit=celcius_to_fahrenheit(orm.temp_high)
            ),
            temp_low=Temperature(
                celcius=orm.temp_low, fahrenheit=celcius_to_fahrenheit(orm.temp_low)
            ),
            temp_avg=Temperature(
                celcius=orm.temp_avg, fahrenheit=celcius_to_fahrenheit(orm.temp_avg)
            ),
        )
