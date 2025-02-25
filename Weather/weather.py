# Name: Robert King
# Assignment: Class Project: Final
# Date: June 3, 2023
# Description: A python program that utilizes the openweathermap.org api and json data
# to retrieve weather information for multiple locations.  The user can enter either a
# zip code or a city name to display weather information for the location.  The information
# currently displayed is as follows: location, weather, current temperature, feels like,
# min temperature, max temperature, humidity, pressure, wind speed, sunrise, and sunset.
# Sources: https://openweathermap.org/ - https://www.instructables.com/Get-Weather-Data-Using-Python-and-Openweather-API/
# https://www.etutorialspoint.com/index.php/388-python-weather-api-script

#Import the request module for making HTTP requests.
import requests
#Import the json module for parsing JSON responses.
import json
#Import datetime module to manipulate UTC time to Standard.
import datetime

#API key for openweathermap.org.
API_KEY = "Your API_Key Here"

#Function to fetch weather data based on city or zip.
def get_weather_data(location):
    try:
        #Check if location is a valid zip code or city name.
        if location.isdigit():
            url = f"https://api.openweathermap.org/data/2.5/weather?zip={location},us&units=imperial&appid={API_KEY}"
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={API_KEY}"
        #Make a GET request to the API url.
        response = requests.get(url)
        #If the response status code is 200 (OK), parse the JSON response and return the weather data.
        if response.status_code == 200:
            #If connection to openweathermap.org successful print message.
            print()
            print("Connection to OpenWeatherMap API successful")
            return json.loads(response.content)
        else:
            #If city or zip is invalid print error message.
            print()
            print("Error: Invalid location")
            return None
    except requests.exceptions.RequestException as e:
        #If connection to openweathermap.org fails print error message.
        print("Error: Failed to connect to OpenWeatherMap API")
        return None

#Function to display weather data based on city or zip submitted by user.
def display_weather_data(weather_data):
    if weather_data is None:
        return
    #Weather data fetched from weather data dictionary.
    name = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    temp_min = weather_data["main"]["temp_min"]
    temp_max = weather_data["main"]["temp_max"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    sunrise_timestamp = weather_data["sys"]["sunrise"]
    sunset_timestamp = weather_data["sys"]["sunset"]
    wind_speed = weather_data["wind"]["speed"]
    weather_desc = weather_data["weather"][0]["description"]

    #Convert sunrise and sunset timestamps to datetime objects.
    sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp)
    sunset = datetime.datetime.fromtimestamp(sunset_timestamp)

    #Weather data printed from data fetched from weather data dictionary.
    print()
    print(f"Location:                 {name}, {country}")
    print(f"Current Weather:          {weather_desc}")
    print(f"Current Temperature:      {temp}°F")
    print(f"Feels like:               {feels_like}°F")
    print(f"Low Temperature:          {temp_min}°F")
    print(f"High Temperature:         {temp_max}°F")
    print(f"Humidity:                 {humidity}%")
    print(f"Air Pressure:             {pressure} hPa")
    print(f"Wind Speed:               {wind_speed} mph")
    #Convert sunrise and sunset to standard time.
    print(f"Sunrise (Standard Time):  {sunrise.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Sunset (Standard Time):   {sunset.strftime('%Y-%m-%d %H:%M:%S')} ")
    print()
  
def main():
    #Create an empty list to store locations entered by user.
    locations = []
    #Loop to allow user to enter multiple locations or use 'q' to terminate program.
    while True:
        location = input("Enter a city name or zip code (enter 'q' to exit): ")
        if location.lower() == "q":
            break
        #Function to fetch the weather data for location entered.
        weather_data = get_weather_data(location)
        #If weather data is not none then display the weather data for location.
        if weather_data is not None:
            display_weather_data(weather_data)
            locations.append(location)

#Call the main function to start the program.
if __name__ == "__main__":
    main()
