import pytest

from app.util import celcius_to_fahrenheit


@pytest.mark.parametrize(
    ("celcius", "expected_fahrenheit"),
    [
        (-15.0, 5.0),
        (11.5, 52.7),
        (48.5, 119.3),
    ],
)
def test_celcius_to_fahrenheit(celcius: float, expected_fahrenheit: float) -> None:
    assert celcius_to_fahrenheit(celcius) == expected_fahrenheit
