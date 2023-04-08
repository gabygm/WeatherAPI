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

    finally:
        client.close()
