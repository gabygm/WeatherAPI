from app.utils.constants import WIND_DIRECTION, SCALE_BEAUFORT


def convert_degrees_direction_to_text(direction):
    val = int((direction / 22.5) + .5)
    wind_direction = WIND_DIRECTION[val % len(WIND_DIRECTION)]
    return wind_direction


def convert_speed_wind_to_text(speed: float) -> str:
    speed_text = ''
    for limit, description in SCALE_BEAUFORT:
        if speed >= limit:
            speed_text = description
            break
    return speed_text
