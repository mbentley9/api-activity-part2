import json
import pytest

from api_activity.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_weather_success(client):
    response = client.get(
        "/weather?lat=41.6&lon=-93.6&unit=fahrenheit"
    )
    assert response.status_code == 200

    data = response.get_json()
    assert "hourly" in data


def test_get_weather_missing_params(client):
    response = client.get("/weather")
    assert response.status_code == 400


def test_post_weather_success(client):
    response = client.post(
        "/weather",
        data=json.dumps({
            "lat": 41.6,
            "lon": -93.6,
            "unit": "celsius"
        }),
        content_type="application/json"
    )
    assert response.status_code == 200

    data = response.get_json()
    assert "hourly" in data


def test_post_weather_missing_fields(client):
    response = client.post(
        "/weather",
        data=json.dumps({"lat": 41.6}),
        content_type="application/json"
    )
    assert response.status_code == 400
