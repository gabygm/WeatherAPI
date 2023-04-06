import httpx

URL = ""


def get_weather():
    client = httpx.Client()
    try:
        response = client.get(f"{URL}", params={"q": "", "appid": ""})
        return response.text

    finally:
        client.close()
