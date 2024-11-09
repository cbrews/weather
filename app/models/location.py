from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.measurement import Measurement


class Location(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    lat: float
    long: float

    measurements: list["Measurement"] = Relationship(back_populates="location")
