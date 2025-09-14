# Handling Request Errors with the requests Module

# Write a program that sends a GET request to a server and handles possible errors using exceptions.


### 🇺🇦 Ukrainian version:

# Обробка помилок запитів з модулем requests

# Напишіть програму, яка відправляє GET-запит на сервер і обробляє можливі помилки, використовуючи виключення.

# Write your code here
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
else:
    print("Success!")
    print(response.json())
