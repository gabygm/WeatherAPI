import logging
import os
import asyncio
import httpx
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("URL")
APP_ID = os.getenv("APP_ID")


async def call_service(url, city, country, cnt=12):
    client = httpx.AsyncClient()
    try:
        response = await client.get(f"{BASE_URL}/{url}",
                                    params={"q": f"{city},{country}",
                                            'cnt': cnt, "appid": APP_ID})
        return response
    except httpx.HTTPError as exc:
        logging.error(f"Error consuming weather service - {exc}")


async def get_weather_forecast(city, country):
    weather_response = call_service('weather', city, country)
    forecast_response = call_service('forecast', city, country)
    results = await asyncio.gather(weather_response, forecast_response)
    return results
