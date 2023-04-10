import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_given_a_valid_city_and_country_should_response_status_200(client):
    response = client.get("/weather?city=Bogota&country=co")
    weather = response.json()
    assert response.status_code == 200
    assert response.json().get("location_name") == "Bogota, CO"
    assert "temperature" in weather
    assert "wind" in weather
    assert "cloudiness" in weather
    assert "pressure" in weather
    assert "humidity" in weather
    assert "sunrise" in weather
    assert "sunset" in weather
    assert "geo_coordinates" in weather
    assert "requested_time" in weather
    assert "forecast" in weather


def test_given_a_city_and_country_do_not_exists_should_response_status_404_not_found(client):
    response = client.get("/weather?city=test&country=co")
    assert response.status_code == 404
    assert response.json().get('detail').get('message') == 'city not found'


def test_given_an_invalid_country_should_response_422(client):
    response = client.get("/weather?city=Bogota&country=test")
    assert response.status_code == 422
    assert response.json().get('detail')[0].get('msg') == 'ensure this value has at most 2 characters'




