# Creating Another Web Server.
#
# Write a web server in Python
# that returns a simple HTML page.
#
# Use http.server.SimpleHTTPRequestHandler.
#
# ```html
#
# <!DOCTYPE html>
#
# <html lang="en">
#
# <head>
#
# <meta charset="UTF-8">
#
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
#
# <title>My First Page</title>
#
# </head>
#
# <body>
#
# <h1>Good news, everyone!</h1>
#
# <p>This is my first HTML page.</p>
#
# <a href="https://www.google.com" target="_blank">Go to Google</a>
#
# </body>
#
# </html>
#
# ```
#
# Requirements:
#
# 1. The program must import
#    the http.server module
#    to create a web server.
# 2. The program must use
#    the SimpleHTTPRequestHandler class
#    to handle HTTP requests.
# 3. The web server must return
#    the specified HTML document
#    when the server is accessed.
# 4. The server must correctly accept
#    and handle incoming requests
#    from the user's browser.
#
# 🇺🇦 Ukrainian version:
#
# Створення ще одного веб-сервера.
#
# Напиши web-сервер на Python,
# який повертає просту HTML-сторінку.
#
# Використовуй http.server.SimpleHTTPRequestHandler.
#
# ```html
#
# <!DOCTYPE html>
#
# <html lang="uk">
#
# <head>
#
# <meta charset="UTF-8">
#
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
#
# <title>Моя перша сторінка</title>
#
# </head>
#
# <body>
#
# <h1>Good news, everyone!</h1>
#
# <p>Це моя перша HTML-сторінка.</p>
#
# <a href="https://www.google.com" target="_blank">Перейти на Google</a>
#
# </body>
#
# </html>
#
# ```
#
# Вимоги:
#
# 1. Програма повинна імпортувати
#    модуль http.server
#    для створення веб-сервера.
# 2. Програма повинна використовувати
#    клас SimpleHTTPRequestHandler
#    для обробки HTTP-запитів.
# 3. Веб-сервер має повертати
#    вказаний HTML-документ
#    при зверненні до сервера.
# 4. Сервер повинен коректно приймати
#    та обробляти вхідні запити
#    від браузера користувача.

from http.server import SimpleHTTPRequestHandler, HTTPServer

# HTML content that should be returned when accessing the server
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Page</title>
</head>
<body>
    <h1>Good news, everyone!</h1>
    <p>This is my first HTML page.</p>
    <a href="https://www.google.com" target="_blank">Go to Google</a>
</body>
</html>
"""

# Create a request handler class inherited from SimpleHTTPRequestHandler
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Override the do_GET method to handle GET requests
    def do_GET(self):
        # Set the HTTP response code (200 - OK)
        self.send_response(200)

        # Specify the response header indicating that the returned content is HTML
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # Send the HTML content in the response
        self.wfile.write(HTML_CONTENT.encode("utf-8"))

# Specify the server parameters: IP address and port
server_address = ("localhost", 8000)  # '' means that the server will be available on all interfaces

# Create a web server using the custom request handler
with HTTPServer(server_address, CustomHTTPRequestHandler) as server:
    # Start the server and wait for incoming requests
    server.serve_forever()