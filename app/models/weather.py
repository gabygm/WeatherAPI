from pydantic import BaseModel

from app.models.forecast import Forecast
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
    forecast: dict

    @classmethod
    def map_data(cls, data_weather, data_forecast):
        weather_response = None
        if data_weather:
            temp = data_weather.get('main').get('temp')
            temp_celsius = temp_to_celsius(temp)
            temp_fahrenheit = temp_to_fahrenheit(temp)
            wind = data_weather.get('wind')
            wind_speed = wind.get('speed')
            wind_direction = convert_degrees_direction_to_text(wind.get('deg'))
            wind_speed_text = convert_speed_wind_to_text(wind_speed)
            forecast_list = map_list_forecast(data_forecast)
            return cls(
                location_name=f"{data_weather.get('name')}, {data_weather.get('sys').get('country')}",
                temperature=f"{temp_celsius}, {temp_fahrenheit}",
                wind=f"{wind_speed_text}, {wind_speed} m/s, {wind_direction}",
                cloudiness=f"{data_weather.get('weather')[0].get('description')}",
                pressure=f"{data_weather.get('main').get('pressure')} hpa",
                humidity=f"{data_weather.get('main').get('humidity')}%",
                sunrise=f"{get_hour_time(data_weather.get('sys').get('sunrise'))}",
                sunset=f"{get_hour_time(data_weather.get('sys').get('sunset'))}",
                geo_coordinates=f"[{round(data_weather.get('coord').get('lat'), 2)}, "
                                f"{round(data_weather.get('coord').get('lon'), 2)}]",
                requested_time=f"{convert_date_time(data_weather.get('dt'))}",
                forecast={
                   'next_weathers': forecast_list
                }
            )

        return weather_response


def map_list_forecast(data):
    list_forecast = []
    for forecast_day in data.get('list'):
        forecast = Forecast.map_data(forecast_day)
        list_forecast.append(forecast)
    return list_forecast

