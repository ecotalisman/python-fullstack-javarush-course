# Publishing Multiple Ports
# Run a container with Nginx and publish ports for HTTP and HTTPS:
# 8080 for HTTP (port 80 inside the container) and 8443 for HTTPS (port 443 inside the container).
# The web server must be available at http://localhost:8080 and https://localhost:8443.
#
# Requirements:
# • The container must be started using the Nginx image to provide web server functionality.
# • The container must publish host port 8080, which is forwarded to port 80 inside the container for handling HTTP requests.
# • The container must publish host port 8443, which is forwarded to port 443 inside the container for handling HTTPS requests.
# • The web server must be available at http://localhost:8080, ensuring correct routing of HTTP requests.
# • The web server must be available at https://localhost:8443, ensuring correct routing of HTTPS requests.
#
# ## 🇺🇦 Ukrainian version:
#
# Публікація кількох портів
# Запустіть контейнер із Nginx та опублікуйте порти для HTTP та HTTPS:
# 8080 для HTTP (порт 80 у контейнері) і 8443 для HTTPS (порт 443 у контейнері).
# Вебсервер повинен бути доступним за адресами http://localhost:8080 та https://localhost:8443.
#
# Вимоги:
# • Контейнер має бути запущений із використанням образу Nginx для забезпечення роботи вебсерверу.
# • Контейнер повинен публікувати порт 8080 хоста, який перенаправляється на порт 80 всередині контейнера для обробки HTTP-запитів.
# • Контейнер повинен публікувати порт 8443 хоста, який перенаправляється на порт 443 всередині контейнера для обробки HTTPS-запитів.
# • Вебсервер повинен бути доступним за адресою http://localhost:8080, забезпечуючи коректну маршрутизацію HTTP-запитів.
# • Вебсервер повинен бути доступним за адресою https://localhost:8443, забезпечуючи коректну маршрутизацію HTTPS-запитів.

# Running a container with port forwarding for HTTP and HTTPS
docker run -d -p 8080:80 -p 8443:443 nginxdemos/hello