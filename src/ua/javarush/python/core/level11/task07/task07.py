# Using the requests Package

# Use the requests package to perform a GET request to an API.
# Perform the following steps:
# - Install the requests package using pip.
# - Use the requests package to perform a GET request to an API, for example, https://jsonplaceholder.typicode.com.
# - Print the result of the request.

### 🇺🇦 Ukrainian version:

# Використання пакета requests.

# Використайте пакет requests для виконання GET-запиту до API.
# Виконайте наступні кроки:
# Встановіть пакет requests за допомогою pip.
# Використайте пакет requests для виконання GET-запиту до API, наприклад, до https://jsonplaceholder.typicode.com.
# Виведіть на екран результат запиту.

# Install the package
# python -m pip install requests

# Example usage:
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

