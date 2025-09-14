# Creating a Socket Client

# Write a program that creates a socket client,
# connects to a socket server, sends it a message, and receives a response.

### 🇺🇦 Ukrainian version:

# Створення сокет-клієнта

# Напишіть програму, яка створює сокет-клієнта,
# підключається до сокет-сервера, відправляє йому повідомлення та отримує відповідь.

# Write your code here
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))
client_socket.sendall(b"Hello, server!")

data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

client_socket.close()
