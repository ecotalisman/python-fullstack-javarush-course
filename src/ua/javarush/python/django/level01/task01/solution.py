# Creating a Web Server.
#
# Write the simplest web server in Python
# that returns the string "Good news, everyone!".
#
# Use http.server.SimpleHTTPRequestHandler.
#
# Requirements:
#
# 1. The program must use the standard http.server module
#    to create a web server.
# 2. The program must define a class
#    that inherits from http.server.SimpleHTTPRequestHandler
#    to handle HTTP requests.
# 3. The program must override the do_GET() method
#    in the handler class
#    to return the string "Good news, everyone!".
# 4. When the server is accessed through a GET request,
#    it must return the string "Good news, everyone!".
#
# 🇺🇦 Ukrainian version:
#
# Створення веб-сервера.
#
# Напиши найпростіший web-сервер на Python,
# який повертає рядок "Good news, everyone!".
#
# Використовуй http.server.SimpleHTTPRequestHandler.
#
# Вимоги:
#
# 1. Програма повинна використовувати стандартний модуль http.server
#    для створення веб-сервера.
# 2. Програма повинна визначити клас,
#    що успадковується від http.server.SimpleHTTPRequestHandler,
#    для обробки HTTP-запитів.
# 3. Програма повинна перевизначати метод do_GET()
#    у класі-обробнику,
#    щоб повертати рядок "Good news, everyone!".
# 4. Під час звернення до сервера через GET-запит,
#    він має повертати рядок "Good news, everyone!".

# Import the necessary classes and modules
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define a class inherited from SimpleHTTPRequestHandler
class CustomHandler(SimpleHTTPRequestHandler):
    # Override the method for handling GET requests
    def do_GET(self):
        # Set the server response as HTTP 200 OK
        self.send_response(200)

        # Specify the response header (content type - plain text)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        # Send the response body with the text "Good news, everyone!"
        self.wfile.write("Good news, everyone!".encode("utf-8"))

# Specify the server parameters: IP address and port
server_address = ('', 8000)  # '' means that the server will be available on all interfaces
httpd = HTTPServer(server_address, CustomHandler)  # Create an instance of the HTTP server

# Start the server and handle requests
httpd.serve_forever()