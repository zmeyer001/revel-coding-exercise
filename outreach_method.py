import json
import requests


def get_weather_info(measurement):
    """
    Given a measurement (i.e. one of the 8 3-hour periods throughout the day), return relevant info.
    Args:
        measurement (dict): Section of the JSON response from the OpenWeatherMap.org API

    Returns:
        (tuple) temp, is_sunny, is_rainy
    """
    temp = measurement["main"]["temp"]
    weather = measurement["weather"][0]["main"]
    is_sunny = True if weather == "Clear" else False
    is_rainy = True if weather == "Rain" else False
    return temp, is_sunny, is_rainy


def get_daily_measurements(data):
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
    # Loop through the data, and grab one set of measurements per day
    daily_measurements = {}     # keys: date, values: (temp, is_sunny, is_rainy)
    for measurement in data["list"]:
        # If we've already grabbed info about this date, move on
        date = measurement["dt_txt"].split(" ")[0]
        if date in daily_measurements:
            continue

        # If the time isn't noon, move on
        time = measurement["dt_txt"].split(" ")[1]
        if time != "12:00:00":
            continue

        # Grab the temperature and sunshine/rain conditions
        if date not in daily_measurements:
            daily_measurements[date] = get_weather_info(measurement)

    return daily_measurements


if __name__ == "__main__":
    # Get data from API
    url = "http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&APPID=09110e603c1d5c272f94f64305c09436"
    response = requests.get(url)
    minneapolis_data = json.loads(response.text)

    # Grab the weather information
    daily_measures = get_daily_measurements(minneapolis_data)
    for day in daily_measures:
        print(day, daily_measures[day])
