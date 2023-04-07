from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_given_a_valid_city_and_country_should_response_status_200():
    response = client.get("/weather?city=Bogota&country=co")
    assert response.status_code == 200



