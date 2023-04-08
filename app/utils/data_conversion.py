from app.utils.constants import KELVIN, WIND_DIRECTION, SCALE_BEAUFORT
from datetime import datetime


def temp_to_celsius(temp) -> str:
    celsius = int(temp - KELVIN)
    return f"{celsius}°C"


def temp_to_fahrenheit(temp) -> str:
    fahrenheit = int((temp - KELVIN) * 1.8 + 32.00)
    return f"{fahrenheit}F"


def get_hour_time(unix):
    datetime_ts = datetime.fromtimestamp(int(unix))
    return datetime_ts.strftime('%H:%M')


def convert_date_time(unix):
    datetime_ts = datetime.fromtimestamp(unix)
    requested_datetime = datetime_ts.strftime('%Y-%m-%d %H:%M:%S')
    return requested_datetime


def convert_degrees_direction_to_text(direction):
    val = int((direction / 22.5) + .5)
    wind_direction = WIND_DIRECTION[val % len(WIND_DIRECTION)]
    return wind_direction


def convert_speed_wind_to_text(speed: float) -> str:
    speed_text = ''
    for limit, description in SCALE_BEAUFORT:
        if speed >= limit:
            return description
    return speed_text
