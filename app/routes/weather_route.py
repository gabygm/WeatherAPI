import json

from fastapi_cache import caches
from fastapi.logger import logger
from fastapi import APIRouter, Query, HTTPException, Depends
from typing_extensions import Annotated
from fastapi_cache.backends.redis import CACHE_KEY, RedisCacheBackend

from app.models.weather import to_weather
from app.services import weather_service as service


router = APIRouter()


def redis_cache():
    return caches.get(CACHE_KEY)


@router.get("/weather")
async def get_weather(city: str,
                      country: Annotated[str, Query(max_length=2)],
                      cache: RedisCacheBackend = Depends(redis_cache)):
    in_cache = await cache.get(f"{city}{country}")
    if not in_cache:
        weather_by_city = service.get_weather(city, country)
        if weather_by_city.status_code == 200:
            weather_response = to_weather(weather_by_city.json())
            await cache.set(key=f"{city}{country}",
                            value=str(weather_response.json()),
                            expire=120)
            return weather_response
        else:
            raise HTTPException(status_code=404, detail=weather_by_city.json())
    logger.info("Consuming data from cache")
    return json.loads(in_cache)
