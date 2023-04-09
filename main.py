import logging
import os
from fastapi import FastAPI
from fastapi_cache import caches
from fastapi_cache.backends.redis import RedisCacheBackend, CACHE_KEY
from dotenv import load_dotenv
from app.routes import weather_route


load_dotenv()
LOGGING = os.getenv("LOGGING")
DB_REDIS = os.getenv("DB_REDIS")

logging.basicConfig(level=LOGGING)
app = FastAPI()
app.include_router(weather_route.router)


@app.on_event('startup')
async def on_startup() -> None:
    rc = RedisCacheBackend(DB_REDIS)
    get_cache = caches.get(CACHE_KEY)
    if not get_cache:
        caches.set(CACHE_KEY, rc)
