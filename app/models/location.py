from typing import TYPE_CHECKING
from pydantic_partial import create_partial_model
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.measurement import Measurement

class Location(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    lat: float
    long: float

    measurements: list["Measurement"] = Relationship(back_populates="location")

LocationCreate = create_partial_model(Location, 'id')