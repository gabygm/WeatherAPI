import logging
import os
import httpx
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")
APP_ID = os.getenv("APP_ID")


def call_service(url, city, country, cnt=1):
    client = httpx.Client()
    try:
        response = client.get(f"{URL}/{url}", params={"q": f"{city},{country}", cnt: cnt, "appid": APP_ID})
        return response
    except httpx.HTTPError as exc:
        logging.error(f"Error consuming weather service - {exc}")
    finally:
        client.close()


def get_weather(city, country):
    response_weather = call_service('weather', city, country)
    return response_weather


def get_forecast(city, country):
    response_weather = call_service('forecast', city, country)
    return response_weather

