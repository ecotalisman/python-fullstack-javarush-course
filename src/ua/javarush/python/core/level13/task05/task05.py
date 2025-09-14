# Sending a GET Request

# Write a program that sends a GET request with parameters to a URL
# and processes the received JSON response.


### 🇺🇦 Ukrainian version:

# Відправка GET-запиту

# Напишіть програму, яка відправляє GET-запит з параметрами на URL та обробляє отриману JSON-відповідь.

# Write your code here
import requests

params = {'userId': 1}
response = requests.get("https://jsonplaceholder.typicode.com/todos/", params=params)
print(response.status_code)
print(response.json())
