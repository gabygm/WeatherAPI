import pytest
from app.services import open_weather_map as service
from app.utils.data_conversion import temp_to_fahrenheit, temp_to_celsius


def test_given_temp_should_covert_to_celsius():
    temp_kelvin = 292.23
    temp_c = temp_to_celsius(temp_kelvin)
    assert temp_c == '19°C'


def test_given_temp_should_covert_to_fahrenheit():
    temp_kelvin = 292.23
    temp_c = temp_to_fahrenheit(temp_kelvin)
    assert temp_c == '66F'


def test_given_a_city_and_country_the_service_should_response_ok(mocker):
    mocker.patch("app.services.open_weather_map.get_weather_by_country", return_value="ok")
    assert service.get_weather_by_country("tes", "test") == "ok"


