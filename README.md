# Software Engineer Coding Exercise
Coding exercise for the Software Engineer position at Revel Health.

## Overview
Using Python, I created a command line application which determines the suggested outreach method for a given city over
the next five days.

_Steps_:
- Using the API for OpenWeatherMap.org, grab the 5-day weather forecast information for the city
- Condense the information for each day into one data point (in this case, I use the weather information at noon)
- Based on the weather information for each day, determine the suggested outreach method

## Software Used
I used the following software to complete this project:
- Windows 10
- Python 3.7
- pytest 5.3.5
- PyCharm 2019.2.2
- GitHub Desktop 2.3.1
- Git Bash 2.23.0
- Notepad++ 7.8.4

## Running the app
Using just the city name:
```commandline
python outreach_method.py "Minneapolis"
```
Note that you can have spaces in the name:
```commandline
python outreach_method.py "Los Angeles"
```
Using the city name and state abbreviation (if city in US):
```commandline
python outreach_method.py "Minneapolis" --state "MN"
```
Using the city name and country code (e.g. if city not in US):
```commandline
python outreach_method.py "London" --country_code "UK"
```

## Testing
Unit tests are written using [`pytest`](https://docs.pytest.org/en/latest/).
To perform the tests, simply run:
```commandline
pytest
```
