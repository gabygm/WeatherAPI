import pdb

from fastapi import APIRouter, Query, HTTPException
from typing_extensions import Annotated

from app.models.weather import to_weather
from app.services import weather_service as service

router = APIRouter()


@router.get("/weather")
def get_weather(city: str, country: Annotated[str, Query(max_length=2)]):
    weather_by_city = service.get_weather_by_city(city, country)
    if weather_by_city.status_code == 200:
        return to_weather(weather_by_city.json())
    raise HTTPException(status_code=404, detail=weather_by_city.json())


