from pydantic import BaseModel

from app.utils.date_time_conversions import get_hour_time, convert_date_time
from app.utils.temperature_conversions import temp_to_celsius, \
                                              temp_to_fahrenheit
from app.utils.wind_conversions import convert_speed_wind_to_text, \
                                       convert_degrees_direction_to_text


class WeatherResponse(BaseModel):
    location_name: str
    temperature: str
    wind: str
    cloudiness: str
    pressure: str
    humidity: str
    sunrise: str
    sunset: str
    geo_coordinates: str
    requested_time: str


def to_weather(data) -> WeatherResponse:
    weather_response = None
    if data:
        temp = data.get('main').get('temp')
        temp_celsius = temp_to_celsius(temp)
        temp_fahrenheit = temp_to_fahrenheit(temp)
        wind = data.get('wind')
        wind_speed = wind.get('speed')
        wind_direction = convert_degrees_direction_to_text(wind.get('deg'))
        wind_speed_text = convert_speed_wind_to_text(wind_speed)

        weather_response = WeatherResponse(
            location_name=f"{data.get('name')}, {data.get('sys').get('country')}",
            temperature=f"{temp_celsius}, {temp_fahrenheit}",
            wind=f"{wind_speed_text}, {wind_speed} m/s, {wind_direction}",
            cloudiness=f"{data.get('weather')[0].get('description')}",
            pressure=f"{data.get('main').get('pressure')} hpa",
            humidity=f"{data.get('main').get('humidity')}%",
            sunrise=f"{get_hour_time(data.get('sys').get('sunrise'))}",
            sunset=f"{get_hour_time(data.get('sys').get('sunset'))}",
            geo_coordinates=f"[{round(data.get('coord').get('lat'), 2)}, "
                            f"{round(data.get('coord').get('lon'), 2)}]",
            requested_time=f"{convert_date_time(data.get('dt'))}"
        )

    return weather_response
