# Performing a POST Request using http.client

# Write a program that performs a POST request to a server with data
# and prints the response. The program should handle possible errors.


### 🇺🇦 Ukrainian version:

# Виконання POST-запиту з використанням http.client

# Напишіть програму, яка виконує POST-запит на сервер з передачею даних і виводить відповідь.
# Програма повинна обробляти можливі помилки.

# Write your code here
import http.client
import json

payload = json.dumps({
    "userId": 1,
    "title": "Learn Python POST request",
    "completed": False
})

headers = {
    "Content-Type": "application/json"
}

try:
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("POST", "/todos", body=payload, headers=headers)
    response = conn.getresponse()
    print(response.status, response.reason)

    data = response.read().decode("utf-8")
    print(data)

except http.client.HTTPConnection as err:
    print(f"HTTPS error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
finally:
    conn.close()
