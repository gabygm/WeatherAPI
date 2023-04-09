from fastapi import FastAPI
from fastapi_cache import caches
from fastapi_cache.backends.redis import RedisCacheBackend, CACHE_KEY

from app.routes import weather_route

app = FastAPI()

app.include_router(weather_route.router)


@app.on_event('startup')
async def on_startup() -> None:
    rc = RedisCacheBackend('redis://localhost')
    get_cache = caches.get(CACHE_KEY)
    if not get_cache:
        caches.set(CACHE_KEY, rc)
