from fastapi import APIRouter, Query
from typing_extensions import Annotated

from app.services import open_weather_map as service
from app.models.weather import *


router = APIRouter()


@router.get("/weather")
def get_weather(city: str, country: Annotated[str, Query(max_length=2)]) -> WeatherResponse:
    weather_city = service.get_weather_by_country(city, country)
    weather_response = map_to_response(weather_city)
    return weather_response


def map_to_response(weather):
    print(weather)
    response_weather = WeatherResponse(
        location_name=f"{weather['name']}, {weather['sys']['country']}",
        temperature=f"{weather['main']['temp']}",
        wind=f"{weather['main']['temp']}",
        cloudiness=f"{weather['weather'][0]['description']}",
        pressure=f"{weather['main']['pressure']} hpa",
        humidity=f"{weather['main']['humidity']} %",
        sunrise=f"{weather['sys']['sunrise']}",
        sunset=f"{weather['sys']['sunset']}",
        geo_coordinates=f"{weather['sys']['sunset']}",
        requested_time=f"[{weather['coord']['lat']}, {weather['coord']['lon']}]",
    )

    return response_weather

