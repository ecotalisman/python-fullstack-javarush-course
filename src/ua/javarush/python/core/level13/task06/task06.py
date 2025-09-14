# Sending a POST Request

# Write a program that sends a POST request with JSON data to a URL
# and processes the received JSON response.


### 🇺🇦 Ukrainian version:

# Відправка POST-запиту

# Напишіть програму, яка відправляє POST-запит з JSON-даними на URL та обробляє отриману JSON-відповідь.

# Write your code here
import requests

data = {
    "userId": 1,
    "title": "Learn Python POST request",
    "completed": False
}

response = requests.post("https://jsonplaceholder.typicode.com/todos/", json=data)
print(response.status_code)
print(response.json())
