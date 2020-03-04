import argparse
import json
import requests

# API key for OpenWeatherMap.org
API_KEY = "09110e603c1d5c272f94f64305c09436"


class CityForecast:

    def __init__(self, city, state, country_code, units, time_of_day):
        self.city = city
        self.state = state
        self.country_code = country_code
        self.units = units
        self.time_of_day = time_of_day
        # Build the URL using the parameters
        self.query = f"{self.city}{',' if self.state else ''}{self.state}{',' if self.country_code else ''}{self.country_code}"
        self.url = f"http://api.openweathermap.org/data/2.5/forecast?q={self.query}&units={self.units}&APPID={API_KEY}"
        self.data = None
        self.outreach_methods = {}    # Keys: date, Values: outreach method

        # Get data from the API
        self.get_data()
        # Determine the best outreach methods for each day
        self.get_outreach_methods()

    def get_data(self):
        """
        Get the 5-day/3-hour forecast from the API for OpenWeatherMap.org.
        Args:
            city (str): City name
            state (str): State abbreviation, if city in US (optional even if in US and city name is unique)
            country_code (str): Country code, as per ISO 3166 (optional if city name is unique)
            units (str): Unit system for temperature
        """
        response = requests.get(self.url)
        self.data = json.loads(response.text)
        if self.data["cod"] == "404":
            raise Exception(f"Problem accessing OpenWeatherMap API: {self.data['message']}")

    def get_outreach_methods(self):
        """
        Given a response from the OpenWeatherMap.org 5-day/3-hour API, grab a summary of temperature, sunshine, and rain for
        each day.
        For now, grabs the conditions at a specific time for each day.  Later, can create a more elegant summary for the day.
        Args:
            data (dict): JSON response from the OpenWeatherMap.org API
            time_of_day (string): Time of day at which the measurements will be collected, formatted in military time as
                HH:MM:SS (e.g. "00:00:00" is midnight)
        """
        # Loop through the data, and grab one set of measurements per day
        for measurement in self.data["list"]:
            # If we've already grabbed info about this date, move on
            date = measurement["dt_txt"].split(" ")[0]
            if date in self.outreach_methods:
                continue

            # If the time isn't the requested time of day, move on
            time = measurement["dt_txt"].split(" ")[1]
            if time != self.time_of_day:
                continue

            # Determine the best outreach method for each day
            self.outreach_methods[date] = DailyMeasurement(measurement).best_method


class DailyMeasurement:

    def __init__(self, data):
        self.data = data
        self.temp = None
        self.is_sunny = None
        self.is_rainy = None
        self.text = None
        self.email = None
        self.phone = None
        self.best_method = None

        # Grab the weather information
        self.get_weather_info()
        # Determine valid outreach methods, given the weather
        self.get_valid_outreach_methods()
        # Determine the best outreach method
        self.choose_outreach_method()

    def get_weather_info(self):
        """
        Given a measurement (i.e. one of the 8 3-hour periods throughout the day), return relevant info.
        """
        self.temp = self.data["main"]["temp"]
        weather = self.data["weather"][0]["main"]
        self.is_sunny = True if weather == "Clear" else False
        self.is_rainy = True if weather == "Rain" else False

    def get_valid_outreach_methods(self):
        """
        Find valid outreach methods, given the weather measurements.
        Rules:
        - Text message: sunny and >75 degrees
        - Email: between 55 and 75 degrees
        - Phone call: <55 degrees or raining
        """
        self.text = True if self.temp >= 75 and self.is_sunny else False
        self.email = True if 55 <= self.temp < 75 and not self.is_rainy else False
        self.phone = True if self.temp < 55 or self.is_rainy else False

    def choose_outreach_method(self):
        """
        Figure out the correct outreach method.
        If there is one valid outreach method, returns that name in a string (e.g. "text")
        Otherwise, returns the string "none".
        """
        if self.text and not (self.email or self.phone):
            self.best_method = "text"
        elif self.email and not self.phone:
            self.best_method = "email"
        elif self.phone:
            self.best_method = "phone"
        else:
            self.best_method = "none"


if __name__ == "__main__":
    # Get arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="City name")
    parser.add_argument("--state", "-s", help="State abbreviation, if city in US", default="")
    parser.add_argument("--country_code", "-cc", help="Country code (ISO 3166)", default="US")
    parser.add_argument("--units", "-u", help="Unit system for temperature", default="imperial")
    parser.add_argument("--time_of_day",
                        "-t",
                        help="Time of day, in military time.  Options: 00:00:00, 03:00:00, 06:00:00, 09:00:00,"
                             "12:00:00, 15:00:00, 18:00:00, 21:00:00)",
                        default="12:00:00")
    args = parser.parse_args()

    # Determine the best outreach method for each day
    forecast = CityForecast(city=args.city, state=args.state, country_code=args.country_code, units=args.units,
                            time_of_day=args.time_of_day)

    # Print out the results
    city_full_string = f"{args.city}{', ' if args.state else ''}{args.state}{', ' if args.country_code else ''}{args.country_code}"
    print(f"Daily outreach methods for {city_full_string}:")
    for date in forecast.outreach_methods:
        print(f"{date}: {forecast.outreach_methods[date]}")
