# Performing a GET Request using http.client

# Write a program that performs a GET request to a server, reads and prints the response.
# The program should handle possible errors.


### 🇺🇦 Ukrainian version:

# Виконання GET-запиту з використанням http.client

# Напишіть програму, яка виконує GET-запит на сервер, читає та виводить відповідь.
# Програма повинна обробляти можливі помилки.

# Write your code here
import http.client
try:
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/todos/1")
    response = conn.getresponse()
    print(response.status, response.reason)

    data = response.read().decode('utf-8')
    print(data)

except http.client.HTTPConnection as err:
    print(f"HTTPS error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
finally:
    conn.close()
