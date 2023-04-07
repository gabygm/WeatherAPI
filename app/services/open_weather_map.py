import os
import httpx
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")
APPID = os.getenv("APPID")


def get_weather_by_country(city, country):
    client = httpx.Client()
    try:
        response = client.get(f"{URL}", params={"q": f"{city},{country}", "appid": APPID})
        return response.json()

    finally:
        client.close()
