# Handling Server Responses with the requests Module

# Write a program that sends a GET request to a server and processes the response,
# including the status code, headers, and response body.

# Write your code here

### 🇺🇦 Ukrainian version:

# Обробка відповідей сервера з модулем requests

# Напишіть програму, яка відправляє GET-запит на сервер і обробляє відповідь, включаючи статус-код, заголовки та тіло відповіді.

# Write your code here
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.headers)
print(response.text)
