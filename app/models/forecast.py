from pydantic import BaseModel

from app.utils.date_time_conversions import convert_date_time
from app.utils.temperature_conversions import temp_to_celsius, temp_to_fahrenheit


class Forecast(BaseModel):
    date: str
    temperature: str
    feels_like: str
    temperature_min: str
    temperature_max: str
    pressure: str
    humidity: str
    description: str

    @classmethod
    def map_data(cls, data):
        temp = data.get('main').get('temp')
        temp_feels_like = data.get('main').get('temp')
        temp_celsius = temp_to_celsius(temp)
        temp_fahrenheit = temp_to_fahrenheit(temp)
        temp_min = data.get('main').get('temp_min')
        temp_max = data.get('main').get('temp_max')

        return cls(
            date=f"{convert_date_time(data.get('dt'))}",
            temperature=f"{temp_celsius}, {temp_fahrenheit}",
            feels_like=f"{temp_to_celsius(temp_feels_like)}",
            temperature_min=f"{temp_to_celsius(temp_min)}",
            temperature_max=f"{temp_to_celsius(temp_max)}",
            pressure=f"{data.get('main').get('pressure')} hpa",
            humidity=f"{data.get('main').get('humidity')}%",
            description=f"{data.get('weather')[0].get('description')}%"
        )

