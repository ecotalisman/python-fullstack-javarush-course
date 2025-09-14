# Using the Google Maps Geocoding API

# Write a program that uses the Google Maps API to retrieve
# the latitude and longitude for a given address.

### 🇺🇦 Ukrainian version:

# Google Maps API

# Напишіть програму, яка використовує Google Maps API для отримання координат
# (широта і довгота) за вказаною адресою.

# Write your code here
import requests

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
address = "1600 Amphitheatre Parkway, Mountain View, CA"
url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
response = requests.get(url)
data = response.json()
if data["status"] == "OK":
    location  = data["results"][0]["geometry"]["location"]
    lat = location["lat"]
    lng = location["lng"]
    print(f"Coordinates: {lat}, {lng}")
else:
    print("Failed to geocode the address")
