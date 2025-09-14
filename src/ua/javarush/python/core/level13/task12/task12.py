# Performing a GET Request through a Proxy using http.client

# Write a program that sends a GET request through a proxy server
# using the http.client library.

### 🇺🇦 Ukrainian version:

# Використання проксі-сервера з модулем http.client

# Напишіть програму, яка відправляє GET-запит через проксі-сервер
# з використанням бібліотеки http.client.

# Write your code here
import http.client

proxy_host = "10.10.1.10"
proxy_port = 3128
dest_url = "httpbin.org"
dest_path = "/ip"

conn = http.client.HTTPSConnection(proxy_host, proxy_port)

conn.set_tunnel(dest_url)
conn.request("GET", dest_path)

response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode("utf-8"))
