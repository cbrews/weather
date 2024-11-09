from datetime import date

from sqlmodel import Field, Relationship, SQLModel

from app.models.location import Location


class Measurement(SQLModel, table=True):
    id: int = Field(primary_key=True)
    location_id: int = Field(foreign_key="location.id")
    date: date
    temp_high: float
    temp_low: float
    temp_avg: float

    location: Location = Relationship(back_populates="measurements")
