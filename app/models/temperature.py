from sqlmodel import SQLModel


class Temperature(SQLModel):
    celcius: float
    fahrenheit: float
