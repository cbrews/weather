import json

from fastapi.testclient import TestClient

from app.models.location import Location


def test_location_apis(client: TestClient) -> None:
    response = client.post(
        url="/location",
        json={
            "city": "Boston",
            "state": "MA",
            "country": "US",
            "lat": 42.372225,
            "long": 71.08501,
        },
    )

    assert response.status_code == 200

    response_json = json.loads(response.text)
    location = Location.model_validate(response_json)

    assert location.id is not None
    assert location.city == "Boston"
    assert location.state == "MA"
    assert location.country == "US"
    assert location.lat == 42.372225
    assert location.long == 71.08501
