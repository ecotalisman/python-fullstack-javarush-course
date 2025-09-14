# Using the OpenWeatherMap API

# Write a program that uses the OpenWeatherMap API
# to get the current weather in a specified city.

### 🇺🇦 Ukrainian version:

# OpenWeatherMap API

# Напишіть програму, яка використовує OpenWeatherMap API
# для отримання поточної погоди в зазначеному місті.

# Write your code here
import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
city = input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    print(f"Weather in {city}: {weather}, temperature: {temp}°C")
else:
    print("Error retrieving weather data")
