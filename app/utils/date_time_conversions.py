from app.utils.constants import KELVIN, WIND_DIRECTION, SCALE_BEAUFORT
from datetime import datetime


def get_hour_time(unix):
    datetime_ts = datetime.fromtimestamp(int(unix))
    return datetime_ts.strftime('%H:%M')


def convert_date_time(unix):
    datetime_ts = datetime.fromtimestamp(unix)
    requested_datetime = datetime_ts.strftime('%Y-%m-%d %H:%M:%S')
    return requested_datetime

