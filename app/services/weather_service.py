import logging
import os
import httpx
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")
APP_ID = os.getenv("APPID")


def get_weather_by_city(city, country):
    client = httpx.Client()
    try:
        response = client.get(f"{URL}/weather", params={"q": f"{city},{country}", "appid": APP_ID})
        return response
    except httpx.HTTPError as exc:
        logging.error(f"Error consuming weather service: {exc.request.url} - {exc}")
    finally:
        client.close()
