from app.utils.constants import KELVIN


def temp_to_celsius(temp) -> str:
    celsius = int(temp - KELVIN)
    return f"{celsius}°C"


def temp_to_fahrenheit(temp) -> str:
    fahrenheit = int((temp - KELVIN) * 1.8 + 32.00)
    return f"{fahrenheit}F"
