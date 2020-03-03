from outreach_method import get_weather_info, get_daily_measurements, get_valid_outreach_methods


def test_get_weather_info_basic():
    measurement = {
        'dt': 1583236800,
        'main': {
            'temp': 28.49,
            'feels_like': 17.04,
            'temp_min': 28.49,
            'temp_max': 28.49,
            'pressure': 999,
            'sea_level': 999,
            'grnd_level': 964,
            'humidity': 86,
            'temp_kf': 0
        },
        'weather': [
            {
                'id': 803,
                'main': 'Clouds',
                'description': 'broken clouds',
                'icon': '04n'
            }
        ],
        'clouds':
            {
                'all': 76
            },
        'wind':
            {
                'speed': 12.33,
                'deg': 274
            },
        'sys':
            {
                'pod': 'n'
            },
        'dt_txt': '2020-03-03 12:00:00'
    }
    assert get_weather_info(measurement) == {'temp': 28.49, 'is_sunny': False, 'is_rainy': False}


def test_get_daily_measurements_basic():
    data = {
        "cod": "200",
        "message": 0,
        "cnt": 40,
        "list": [
            {
                "dt": 1583182800,
                "main": {
                    "temp": 35.67,
                    "feels_like": 27.12,
                    "temp_min": 30.27,
                    "temp_max": 35.67,
                    "pressure": 1007,
                    "sea_level": 1007,
                    "grnd_level": 972,
                    "humidity": 75,
                    "temp_kf": 3
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 7.99,
                    "deg": 226
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-02 21:00:00"
            },
            {
                "dt": 1583193600,
                "main": {
                    "temp": 32.92,
                    "feels_like": 24.37,
                    "temp_min": 28.87,
                    "temp_max": 32.92,
                    "pressure": 1005,
                    "sea_level": 1005,
                    "grnd_level": 969,
                    "humidity": 84,
                    "temp_kf": 2.25
                },
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03d"
                    }
                ],
                "clouds": {
                    "all": 50
                },
                "wind": {
                    "speed": 8.01,
                    "deg": 188
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-03 00:00:00"
            },
            {
                "dt": 1583204400,
                "main": {
                    "temp": 32.41,
                    "feels_like": 22.26,
                    "temp_min": 29.71,
                    "temp_max": 32.41,
                    "pressure": 1002,
                    "sea_level": 1002,
                    "grnd_level": 967,
                    "humidity": 79,
                    "temp_kf": 1.5
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 10.4,
                    "deg": 185
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-03 03:00:00"
            },
            {
                "dt": 1583215200,
                "main": {
                    "temp": 31.89,
                    "feels_like": 21.27,
                    "temp_min": 30.54,
                    "temp_max": 31.89,
                    "pressure": 1000,
                    "sea_level": 1000,
                    "grnd_level": 964,
                    "humidity": 80,
                    "temp_kf": 0.75
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 82
                },
                "wind": {
                    "speed": 11.21,
                    "deg": 209
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-03 06:00:00"
            },
            {
                "dt": 1583226000,
                "main": {
                    "temp": 30.63,
                    "feels_like": 21.83,
                    "temp_min": 30.63,
                    "temp_max": 30.63,
                    "pressure": 999,
                    "sea_level": 999,
                    "grnd_level": 963,
                    "humidity": 86,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 8.08,
                    "deg": 253
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-03 09:00:00"
            },
            {
                "dt": 1583236800,
                "main": {
                    "temp": 28.49,
                    "feels_like": 17.04,
                    "temp_min": 28.49,
                    "temp_max": 28.49,
                    "pressure": 999,
                    "sea_level": 999,
                    "grnd_level": 964,
                    "humidity": 86,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 76
                },
                "wind": {
                    "speed": 12.33,
                    "deg": 274
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-03 12:00:00"
            },
            {
                "dt": 1583247600,
                "main": {
                    "temp": 31.68,
                    "feels_like": 18.61,
                    "temp_min": 31.68,
                    "temp_max": 31.68,
                    "pressure": 1001,
                    "sea_level": 1001,
                    "grnd_level": 966,
                    "humidity": 84,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 64
                },
                "wind": {
                    "speed": 15.75,
                    "deg": 296
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-03 15:00:00"
            },
            {
                "dt": 1583258400,
                "main": {
                    "temp": 34.14,
                    "feels_like": 22.41,
                    "temp_min": 34.14,
                    "temp_max": 34.14,
                    "pressure": 1003,
                    "sea_level": 1003,
                    "grnd_level": 968,
                    "humidity": 78,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 82
                },
                "wind": {
                    "speed": 13.51,
                    "deg": 289
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-03 18:00:00"
            },
            {
                "dt": 1583269200,
                "main": {
                    "temp": 33.46,
                    "feels_like": 22.26,
                    "temp_min": 33.46,
                    "temp_max": 33.46,
                    "pressure": 1004,
                    "sea_level": 1004,
                    "grnd_level": 969,
                    "humidity": 79,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 91
                },
                "wind": {
                    "speed": 12.48,
                    "deg": 281
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-03 21:00:00"
            },
            {
                "dt": 1583280000,
                "main": {
                    "temp": 32.43,
                    "feels_like": 22.28,
                    "temp_min": 32.43,
                    "temp_max": 32.43,
                    "pressure": 1005,
                    "sea_level": 1005,
                    "grnd_level": 970,
                    "humidity": 79,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 95
                },
                "wind": {
                    "speed": 10.4,
                    "deg": 273
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-04 00:00:00"
            },
            {
                "dt": 1583290800,
                "main": {
                    "temp": 29.57,
                    "feels_like": 20.48,
                    "temp_min": 29.57,
                    "temp_max": 29.57,
                    "pressure": 1007,
                    "sea_level": 1007,
                    "grnd_level": 971,
                    "humidity": 86,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 98
                },
                "wind": {
                    "speed": 8.37,
                    "deg": 267
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-04 03:00:00"
            },
            {
                "dt": 1583301600,
                "main": {
                    "temp": 28.06,
                    "feels_like": 19.36,
                    "temp_min": 28.06,
                    "temp_max": 28.06,
                    "pressure": 1008,
                    "sea_level": 1008,
                    "grnd_level": 973,
                    "humidity": 85,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 95
                },
                "wind": {
                    "speed": 7.31,
                    "deg": 300
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-04 06:00:00"
            },
            {
                "dt": 1583312400,
                "main": {
                    "temp": 26.29,
                    "feels_like": 16.23,
                    "temp_min": 26.29,
                    "temp_max": 26.29,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 975,
                    "humidity": 84,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03n"
                    }
                ],
                "clouds": {
                    "all": 50
                },
                "wind": {
                    "speed": 9.37,
                    "deg": 301
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-04 09:00:00"
            },
            {
                "dt": 1583323200,
                "main": {
                    "temp": 24.71,
                    "feels_like": 15.44,
                    "temp_min": 24.71,
                    "temp_max": 24.71,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 977,
                    "humidity": 84,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 51
                },
                "wind": {
                    "speed": 7.67,
                    "deg": 292
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-04 12:00:00"
            },
            {
                "dt": 1583334000,
                "main": {
                    "temp": 27.48,
                    "feels_like": 19.04,
                    "temp_min": 27.48,
                    "temp_max": 27.48,
                    "pressure": 1016,
                    "sea_level": 1016,
                    "grnd_level": 980,
                    "humidity": 81,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "few clouds",
                        "icon": "02d"
                    }
                ],
                "clouds": {
                    "all": 20
                },
                "wind": {
                    "speed": 6.55,
                    "deg": 289
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-04 15:00:00"
            },
            {
                "dt": 1583344800,
                "main": {
                    "temp": 33.49,
                    "feels_like": 25.56,
                    "temp_min": 33.49,
                    "temp_max": 33.49,
                    "pressure": 1016,
                    "sea_level": 1016,
                    "grnd_level": 981,
                    "humidity": 74,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 10
                },
                "wind": {
                    "speed": 6.38,
                    "deg": 280
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-04 18:00:00"
            },
            {
                "dt": 1583355600,
                "main": {
                    "temp": 36.39,
                    "feels_like": 30.51,
                    "temp_min": 36.39,
                    "temp_max": 36.39,
                    "pressure": 1015,
                    "sea_level": 1015,
                    "grnd_level": 980,
                    "humidity": 70,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 3.04,
                    "deg": 255
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-04 21:00:00"
            },
            {
                "dt": 1583366400,
                "main": {
                    "temp": 31.87,
                    "feels_like": 23.85,
                    "temp_min": 31.87,
                    "temp_max": 31.87,
                    "pressure": 1016,
                    "sea_level": 1016,
                    "grnd_level": 980,
                    "humidity": 93,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 2
                },
                "wind": {
                    "speed": 7.43,
                    "deg": 202
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-05 00:00:00"
            },
            {
                "dt": 1583377200,
                "main": {
                    "temp": 32.83,
                    "feels_like": 22.98,
                    "temp_min": 32.83,
                    "temp_max": 32.83,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 979,
                    "humidity": 91,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 83
                },
                "wind": {
                    "speed": 10.76,
                    "deg": 176
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-05 03:00:00"
            },
            {
                "dt": 1583388000,
                "main": {
                    "temp": 34.36,
                    "feels_like": 24.85,
                    "temp_min": 34.36,
                    "temp_max": 34.36,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 975,
                    "humidity": 76,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 92
                },
                "wind": {
                    "speed": 9.48,
                    "deg": 171
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-05 06:00:00"
            },
            {
                "dt": 1583398800,
                "main": {
                    "temp": 35.82,
                    "feels_like": 25.93,
                    "temp_min": 35.82,
                    "temp_max": 35.82,
                    "pressure": 1009,
                    "sea_level": 1009,
                    "grnd_level": 974,
                    "humidity": 73,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 10.25,
                    "deg": 219
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-05 09:00:00"
            },
            {
                "dt": 1583409600,
                "main": {
                    "temp": 37.22,
                    "feels_like": 25.3,
                    "temp_min": 37.22,
                    "temp_max": 37.22,
                    "pressure": 1010,
                    "sea_level": 1010,
                    "grnd_level": 975,
                    "humidity": 88,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 15.35,
                    "deg": 282
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-05 12:00:00"
            },
            {
                "dt": 1583420400,
                "main": {
                    "temp": 36.23,
                    "feels_like": 22.08,
                    "temp_min": 36.23,
                    "temp_max": 36.23,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 977,
                    "humidity": 70,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "few clouds",
                        "icon": "02d"
                    }
                ],
                "clouds": {
                    "all": 18
                },
                "wind": {
                    "speed": 17.67,
                    "deg": 282
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-05 15:00:00"
            },
            {
                "dt": 1583431200,
                "main": {
                    "temp": 36.54,
                    "feels_like": 20.61,
                    "temp_min": 36.54,
                    "temp_max": 36.54,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 978,
                    "humidity": 66,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03d"
                    }
                ],
                "clouds": {
                    "all": 25
                },
                "wind": {
                    "speed": 20.58,
                    "deg": 288
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-05 18:00:00"
            },
            {
                "dt": 1583442000,
                "main": {
                    "temp": 33.4,
                    "feels_like": 16.57,
                    "temp_min": 33.4,
                    "temp_max": 33.4,
                    "pressure": 1016,
                    "sea_level": 1016,
                    "grnd_level": 980,
                    "humidity": 75,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 22.21,
                    "deg": 302
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-05 21:00:00"
            },
            {
                "dt": 1583452800,
                "main": {
                    "temp": 31.77,
                    "feels_like": 15.17,
                    "temp_min": 31.77,
                    "temp_max": 31.77,
                    "pressure": 1019,
                    "sea_level": 1019,
                    "grnd_level": 984,
                    "humidity": 73,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 21.34,
                    "deg": 319
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-06 00:00:00"
            },
            {
                "dt": 1583463600,
                "main": {
                    "temp": 31.32,
                    "feels_like": 16.95,
                    "temp_min": 31.32,
                    "temp_max": 31.32,
                    "pressure": 1024,
                    "sea_level": 1024,
                    "grnd_level": 988,
                    "humidity": 75,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 99
                },
                "wind": {
                    "speed": 17.43,
                    "deg": 330
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-06 03:00:00"
            },
            {
                "dt": 1583474400,
                "main": {
                    "temp": 29.39,
                    "feels_like": 17.31,
                    "temp_min": 29.39,
                    "temp_max": 29.39,
                    "pressure": 1027,
                    "sea_level": 1027,
                    "grnd_level": 991,
                    "humidity": 79,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 98
                },
                "wind": {
                    "speed": 13.24,
                    "deg": 326
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-06 06:00:00"
            },
            {
                "dt": 1583485200,
                "main": {
                    "temp": 27.23,
                    "feels_like": 16.43,
                    "temp_min": 27.23,
                    "temp_max": 27.23,
                    "pressure": 1030,
                    "sea_level": 1030,
                    "grnd_level": 993,
                    "humidity": 82,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 4
                },
                "wind": {
                    "speed": 10.74,
                    "deg": 325
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-06 09:00:00"
            },
            {
                "dt": 1583496000,
                "main": {
                    "temp": 25.79,
                    "feels_like": 16.86,
                    "temp_min": 25.79,
                    "temp_max": 25.79,
                    "pressure": 1032,
                    "sea_level": 1032,
                    "grnd_level": 995,
                    "humidity": 82,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 4
                },
                "wind": {
                    "speed": 7.16,
                    "deg": 340
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-06 12:00:00"
            },
            {
                "dt": 1583506800,
                "main": {
                    "temp": 28.49,
                    "feels_like": 21.63,
                    "temp_min": 28.49,
                    "temp_max": 28.49,
                    "pressure": 1033,
                    "sea_level": 1033,
                    "grnd_level": 997,
                    "humidity": 72,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 3.42,
                    "deg": 350
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-06 15:00:00"
            },
            {
                "dt": 1583517600,
                "main": {
                    "temp": 34.54,
                    "feels_like": 27.45,
                    "temp_min": 34.54,
                    "temp_max": 34.54,
                    "pressure": 1033,
                    "sea_level": 1033,
                    "grnd_level": 997,
                    "humidity": 51,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 3.44,
                    "deg": 158
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-06 18:00:00"
            },
            {
                "dt": 1583528400,
                "main": {
                    "temp": 37.49,
                    "feels_like": 28.8,
                    "temp_min": 37.49,
                    "temp_max": 37.49,
                    "pressure": 1031,
                    "sea_level": 1031,
                    "grnd_level": 994,
                    "humidity": 48,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 6.51,
                    "deg": 169
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-06 21:00:00"
            },
            {
                "dt": 1583539200,
                "main": {
                    "temp": 33.15,
                    "feels_like": 23.63,
                    "temp_min": 33.15,
                    "temp_max": 33.15,
                    "pressure": 1029,
                    "sea_level": 1029,
                    "grnd_level": 993,
                    "humidity": 64,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 8.43,
                    "deg": 158
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-07 00:00:00"
            },
            {
                "dt": 1583550000,
                "main": {
                    "temp": 31.78,
                    "feels_like": 20.79,
                    "temp_min": 31.78,
                    "temp_max": 31.78,
                    "pressure": 1028,
                    "sea_level": 1028,
                    "grnd_level": 992,
                    "humidity": 57,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 10.38,
                    "deg": 160
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-07 03:00:00"
            },
            {
                "dt": 1583560800,
                "main": {
                    "temp": 33.13,
                    "feels_like": 20.89,
                    "temp_min": 33.13,
                    "temp_max": 33.13,
                    "pressure": 1025,
                    "sea_level": 1025,
                    "grnd_level": 989,
                    "humidity": 56,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 0
                },
                "wind": {
                    "speed": 12.73,
                    "deg": 163
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-07 06:00:00"
            },
            {
                "dt": 1583571600,
                "main": {
                    "temp": 34.32,
                    "feels_like": 21.4,
                    "temp_min": 34.32,
                    "temp_max": 34.32,
                    "pressure": 1021,
                    "sea_level": 1021,
                    "grnd_level": 985,
                    "humidity": 57,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "few clouds",
                        "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 11
                },
                "wind": {
                    "speed": 14.18,
                    "deg": 169
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-07 09:00:00"
            },
            {
                "dt": 1583582400,
                "main": {
                    "temp": 34.09,
                    "feels_like": 21.7,
                    "temp_min": 34.09,
                    "temp_max": 34.09,
                    "pressure": 1019,
                    "sea_level": 1019,
                    "grnd_level": 984,
                    "humidity": 64,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 8
                },
                "wind": {
                    "speed": 13.69,
                    "deg": 180
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-03-07 12:00:00"
            },
            {
                "dt": 1583593200,
                "main": {
                    "temp": 37.65,
                    "feels_like": 25.12,
                    "temp_min": 37.65,
                    "temp_max": 37.65,
                    "pressure": 1017,
                    "sea_level": 1017,
                    "grnd_level": 982,
                    "humidity": 62,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 98
                },
                "wind": {
                    "speed": 14.47,
                    "deg": 187
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-07 15:00:00"
            },
            {
                "dt": 1583604000,
                "main": {
                    "temp": 44.4,
                    "feels_like": 32.59,
                    "temp_min": 44.4,
                    "temp_max": 44.4,
                    "pressure": 1015,
                    "sea_level": 1015,
                    "grnd_level": 980,
                    "humidity": 57,
                    "temp_kf": 0
                },
                "weather": [
                    {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 93
                },
                "wind": {
                    "speed": 14.14,
                    "deg": 184
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-03-07 18:00:00"
            }
        ],
        "city": {
            "id": 5037649,
            "name": "Minneapolis",
            "coord": {
                "lat": 44.98,
                "lon": -93.2638
            },
            "country": "US",
            "population": 382578,
            "timezone": -21600,
            "sunrise": 1583153303,
            "sunset": 1583193726
        }
    }
    assert get_daily_measurements(data) == {'2020-03-03': {'temp': 28.49, 'is_sunny': False, 'is_rainy': False}, '2020-03-04': {'temp': 24.71, 'is_sunny': False, 'is_rainy': False}, '2020-03-05': {'temp': 37.22, 'is_sunny': False, 'is_rainy': False}, '2020-03-06': {'temp': 25.79, 'is_sunny': True, 'is_rainy': False}, '2020-03-07': {'temp': 34.09, 'is_sunny': True, 'is_rainy': False}}


def test_get_valid_outreach_methods_basic():
    measures = {
        '2020-03-03': {"temp": 28.49, "is_sunny": False, "is_rainy": False},
        '2020-03-04': {"temp": 24.71, "is_sunny": False, "is_rainy": False},
        '2020-03-05': {"temp": 37.22, "is_sunny": False, "is_rainy": False},
        '2020-03-06': {"temp": 25.79, "is_sunny": True, "is_rainy": False},
        '2020-03-07': {"temp": 34.09, "is_sunny": True, "is_rainy": False}
    }
    assert get_valid_outreach_methods(measures) == {'2020-03-03': {'text': False, 'email': False, 'phone': True}, '2020-03-04': {'text': False, 'email': False, 'phone': True}, '2020-03-05': {'text': False, 'email': False, 'phone': True}, '2020-03-06': {'text': False, 'email': False, 'phone': True}, '2020-03-07': {'text': False, 'email': False, 'phone': True}}
