import pytest
from app.services import open_weather_map as service
from app.utils.data_conversion import temp_to_fahrenheit, temp_to_celsius, get_hour_time, \
    convert_degrees_direction_to_text, convert_speed_wind_to_text
from  app.models import weather
from app.routers.weather import map_to_response
from tests.fakers import weather_fake_consume_api, weather_fake_data_response


class TestConversionData:

    def test_given_temp_should_covert_to_celsius(self):
        temp_kelvin = 292.23
        temp_c = temp_to_celsius(temp_kelvin)
        assert temp_c == '19°C'

    def test_given_temp_should_covert_to_fahrenheit(self):
        temp_kelvin = 292.23
        temp_c = temp_to_fahrenheit(temp_kelvin)
        assert temp_c == '66F'

    def test_given_unix_should_covert_to_hour_time(self):
        unix = 1680995941
        hour_time = get_hour_time(unix)
        assert hour_time == '18:19'

    def test_given_degrees_with_value_zero_should_covert_to_direction_north(self):
        degrees = 0
        direction = convert_degrees_direction_to_text(degrees)
        assert direction == 'North'

    def test_given_speed_with_value_less_than_2_should_covert_to_text(self):
        degrees = 1.5
        direction = convert_speed_wind_to_text(degrees)
        assert direction == 'Light air'


class TestWeather:
    def test_given_a_right_data_should_map_to_weather_response(self):
        weather_response = map_to_response(weather_fake_consume_api)
        assert weather_response.location_name == weather_fake_data_response.get('location_name')
        assert weather_response.temperature == weather_fake_data_response.get('temperature')
        assert weather_response.wind == weather_fake_data_response.get('wind')
        assert weather_response.cloudiness == weather_fake_data_response.get('cloudiness')
        assert weather_response.pressure == weather_fake_data_response.get('pressure')
        assert weather_response.humidity == weather_fake_data_response.get('humidity')
        assert weather_response.sunrise == weather_fake_data_response.get('sunrise')
        assert weather_response.sunset == weather_fake_data_response.get('sunset')
        assert weather_response.geo_coordinates == weather_fake_data_response.get('geo_coordinates')
        assert weather_response.requested_time == weather_fake_data_response.get('requested_time')

    def test_given_a_empty_data_should_response(self):
        weather_response = map_to_response({})
        assert weather_response is None





