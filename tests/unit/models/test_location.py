import pytest

from app.models import Location


def test_location_orm__ok() -> None:
    location = Location(
        city="Boston",
        state="MA",
        country="US",
        lat=42.372225,
        long=71.08501,
    )

    assert isinstance(location, Location)
    assert location.city == "Boston"


def test_location_orm__bad() -> None:
    with pytest.raises(ValueError) as exc_info:
        Location(
            city="London",
            state="UK",
            country="UK",
            lat=72.01,
            long=72.04,
        )

        assert str(exc_info.value) == "We only support US cities at this time!"
