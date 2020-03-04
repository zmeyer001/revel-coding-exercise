# Software Engineer Coding Exercise
Coding exercise for the Software Engineer position at Revel Health.

## Overview
Using Python, I created a command line application which determines the suggested outreach method for a given city over
the next five days.

_Steps_:
- Using the API for OpenWeatherMap.org, grab the 5-day weather forecast information for the city
- Condense the information for each day into one data point (user supplies which hour of day to use)
- Based on the weather information for each day at the given hour, determine the suggested outreach method

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

## Project limitations
If I were to have more time to work on this project, I would make a variety of tweaks to my code:
- Summarize daily weather: Instead of using the weather from the same hour for each day, I would create a more elegant
summary.  For example, I could summarize the day's weather using the average values for the temperatures, sunshine, and
rain.
- Enhance communication method selection: Determine a valid method of communication for cases where the temperature is
greater than 75 degrees Fahrenheit and it is not sunny.  Currently, I return `"none"` in these rare cases.  Also, if
there were two valid methods of communication for the same day, I'd currently return `"none"`.
- Use other technologies: Most of my coding experience thus far has been in Python, so it would be fun to learn how to
create this application using other technologies like Java and JavaScript.  Also, I have a little bit of experience
creating Flask services, so it would have been fun to work with those again.
- Add tests: When I first started the project, I was doing some procedural programming, and had written a basic unit
test for each function that I created.  Then I pivoted to using object-oriented programming, and the refactor broke my
tests.  With more time, I would have mocked the API call and fixed the tests.
- Increase performance: In my normal practice, after creating a minimum viable product, I go back and increase the
efficiency of my code.
