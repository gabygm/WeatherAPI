import pytest
from app.services import open_weather_map as service


def test_given_a_city_and_country_the_service_should_response_ok(mocker):
    mocker.patch("app.services.open_weather_map.get_weather_by_country", return_value="ok")
    assert service.get_weather_by_country("tes", "test") == "ok"

