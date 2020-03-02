import json
import requests


def get_weather_info(data):
    """
    Given a response from the OpenWeatherMap.org 5-day/3-hour API, grab a summary of temperature, sunshine, and rain for
    each day.
    For now, grab the conditions at noon for each day.  The assumption is that communication will occur in the middle of
    the day. Later, can create a more elegant summary for the day.
    Args:
        data (dict): JSON response from the OpenWeatherMap.org API

    Returns:
        (dict) Keys: date, Values: (temp, is_sunny, is_rainy)
    """
    daily_measures = {}     # keys: date, values: (temp, is_sunny, is_rainy)
    for measurement in data["list"]:
        # If we've already grabbed info about this date, move on
        date = measurement["dt_txt"].split(" ")[0]
        if date in daily_measures:
            continue

        # If the time isn't noon, move on
        time = measurement["dt_txt"].split(" ")[1]
        if time != "12:00:00":
            continue

        # Grab the temperature and sunshine/rain conditions
        temp = measurement["main"]["temp"]
        weather = measurement["weather"][0]["main"]
        is_sunny = True if weather == "Clear" else False
        is_rainy = True if weather == "Rain" else False
        if date not in daily_measures:
            daily_measures[date] = (temp, is_sunny, is_rainy)

    return daily_measures


if __name__ == "__main__":
    # Get data from API
    url = "http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&APPID=09110e603c1d5c272f94f64305c09436"
    response = requests.get(url)
    data = json.loads(response.text)

    # Grab the weather information
    daily_measures = get_weather_info(data)
    for day in daily_measures:
        print(day, daily_measures[day])
