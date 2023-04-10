

weather_fake_data_response = {
    "location_name": "Bogota, CO",
    "temperature": "15°C, 60F",
    "wind": "Gentle breeze, 4.12 m/s, West",
    "cloudiness": "light intensity drizzle",
    "pressure": "1026 hpa",
    "humidity": "82%",
    "sunrise": "05:52",
    "sunset": "18:03",
    "geo_coordinates": "[4.61, -74.08]",
    "requested_time": "2023-04-08 13:13:13"
}

weather_fake_consume_api = {
    "coord": {
        "lon": -74.0817,
        "lat": 4.6097
    },
    "weather": [{
        "id": 300,
        "main": "Drizzle",
        "description": "light intensity drizzle",
        "icon": "09d"
        }],
    "base": "stations",
    "main": {
        "temp": 288.88,
        "feels_like": 288.65,
        "temp_min": 288.88,
        "temp_max": 288.88,
        "pressure": 1026,
        "humidity": 82
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.12,
        "deg": 280},
    "clouds": {
        "all": 75},
    "dt": 1680977593,
    "sys": {
        "type": 1,
        "id": 8582,
        "country": "CO",
        "sunrise": 1680951140,
        "sunset": 1680995022},
    "timezone": -18000,
    "id": 3688689,
    "name": "Bogota",
    "cod": 200
    }

forecast_fake_consume_api = {
    "cod": "200",
    "message": 0,
    "cnt": 1,
    "list": [
        {"dt": 1681160400,
         "main": {
             "temp": 290.14,
             "feels_like": 289.62,
             "temp_min": 288.67,
             "temp_max": 290.14,
             "pressure": 1022,
             "sea_level": 1022,
             "grnd_level": 752,
             "humidity": 66,
             "temp_kf": 1.47
            },
         "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
         "clouds": {
            "all": 80
        },
         "wind": {
            "speed": 1.21,
            "deg": 147,
            "gust": 2.28
            },
         "rain": {
            "3h": 2.21
            },
         "sys": {
            "pod": "d"
            },
         "dt_txt": "2023-04-10 21:00:00"}
    ],}