# Creating a Socket Server

# Write a program that creates a socket server,
# accepts incoming connections from clients and responds with "Hello, client!".

### 🇺🇦 Ukrainian version:

# Створення сокет-сервера

# Напишіть програму, яка створює сокет-сервер,
# приймає вхідні з'єднання від клієнтів і відповідає їм "Hello, client!".

# Write your code here
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(5)

print("Server is waiting for connection...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    data = client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    client_socket.sendall(b"Hello, client!")
    client_socket.close()
