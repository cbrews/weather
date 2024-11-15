from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import validates
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.measurement import Measurement


class Location(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    city: str
    state: str
    country: str
    lat: float
    long: float

    measurements: list["Measurement"] = Relationship(back_populates="location")

    __table_args__ = (
        UniqueConstraint("city", "state", "country", name="city_state_country"),
    )

    @validates("country")
    def validates_country(self, key: str, value: str) -> str:
        if value != "US":
            raise ValueError("We only support US cities at this time!")
        return value


class LocationPartial(SQLModel):
    city: str | None
    state: str | None
    country: str | None
    lat: float | None
    long: float | None
