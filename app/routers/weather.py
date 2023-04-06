from fastapi import APIRouter
from app.services import openweathermap

router = APIRouter()


@router.get("/weather")
def get_weather(city, country):
    weather_city = openweathermap.get_weather()
    return {"message": f"Hello world {city} {weather_city}"}