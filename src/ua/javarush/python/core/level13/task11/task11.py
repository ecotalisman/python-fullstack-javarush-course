# Performing a GET Request through a Proxy using requests

# Write a program that sends a GET request through a proxy server
# using the requests library.

### 🇺🇦 Ukrainian version:

# Використання проксі-сервера з модулем requests

# Напишіть програму, яка відправляє GET-запит через проксі-сервер
# з використанням бібліотеки requests.

# Write your code here
import requests

url = "http://httpbin.org/ip"
proxies = {
    "http":  "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
response = requests.get(url, proxies=proxies)
print(response.json())
