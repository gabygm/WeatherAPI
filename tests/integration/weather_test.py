import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_given_a_valid_city_and_country_should_response_status_200(client):
    response = client.get("/weather?city=Bogota&country=co")
    assert response.status_code == 200
    assert response.json().get("location_name") == "Bogota, CO"
    assert response.json().get("temperature") is not None
    assert response.json().get("wind") is not None
    assert response.json().get("cloudiness") is not None
    assert response.json().get("pressure") is not None
    assert response.json().get("humidity") is not None
    assert response.json().get("sunrise") is not None
    assert response.json().get("sunset") is not None
    assert response.json().get("geo_coordinates") is not None
    assert response.json().get("requested_time") is not None


def test_given_a_city_and_country_do_not_exists_should_response_status_404_not_found(client):
    response = client.get("/weather?city=test&country=co")
    assert response.status_code == 404
    assert response.json().get('detail').get('message') == 'city not found'


def test_given_an_invalid_country_should_response_422(client):
    response = client.get("/weather?city=Bogota&country=test")
    assert response.status_code == 422
    assert response.json().get('detail')[0].get('msg') == 'ensure this value has at most 2 characters'




