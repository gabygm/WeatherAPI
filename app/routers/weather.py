from fastapi import APIRouter, Query
from typing_extensions import Annotated

from app.services import open_weather_map as service
from app.models.weather import *
from app.utils.data_conversion import temp_to_celsius, temp_to_fahrenheit, get_hour_time, convert_date_time, \
    convert_degrees_direction_to_text, convert_speed_wind_to_text

router = APIRouter()


@router.get("/weather")
def get_weather(city: str, country: Annotated[str, Query(max_length=2)]) -> WeatherResponse:
    weather_city = service.get_weather_by_country(city, country)
    weather_response = map_to_response(weather_city)
    return weather_response


def map_to_response(weather):
    response_weather = None
    if weather:
        temp = weather.get('main').get('temp')
        temp_celsius = temp_to_celsius(temp)
        temp_fahrenheit = temp_to_fahrenheit(temp)
        wind = weather.get('wind')
        wind_speed = wind.get('speed')
        wind_direction = convert_degrees_direction_to_text(wind.get('deg'))
        wind_speed_text = convert_speed_wind_to_text(wind_speed)

        response_weather = WeatherResponse(
            location_name=f"{weather.get('name')}, {weather.get('sys').get('country')}",
            temperature=f"{temp_celsius}, {temp_fahrenheit}",
            wind=f"{wind_speed_text}, {wind_speed} m/s, {wind_direction}",
            cloudiness=f"{weather.get('weather')[0].get('description')}",
            pressure=f"{weather.get('main').get('pressure')} hpa",
            humidity=f"{weather.get('main').get('humidity')}%",
            sunrise=f"{get_hour_time(weather.get('sys').get('sunrise'))}",
            sunset=f"{get_hour_time(weather.get('sys').get('sunset'))}",
            geo_coordinates=f"[{round(weather.get('coord').get('lat'), 2)}, {round(weather.get('coord').get('lon'), 2)}]",
            requested_time=f"{convert_date_time(weather.get('dt'))}"
        )

    return response_weather

