from app.models.location import Location
import json


def test_location_apis(client):
    response = client.post(
        url="/location",
        json={
            "name": "Boston",
            "lat": 42.372225,
            "long": 71.08501,
        },
    )

    assert response.status_code == 200

    response_json = json.loads(response.text)
    location = Location.model_validate(response_json)

    assert location.id is not None
    assert location.name == "Boston"
    assert location.lat == 42.372225
    assert location.long == 71.08501
