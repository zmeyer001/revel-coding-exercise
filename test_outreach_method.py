from outreach_method import get_weather_info


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
    assert get_weather_info(measurement) == (28.49, False, False)


if __name__ == '__main__':
    test_get_weather_info_basic()
    print("Everything passed")
