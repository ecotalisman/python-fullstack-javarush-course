# Publishing Ports with IP Restriction
# Run a container with Nginx, publish container port 80 to host port 8080,
# but restrict access only to the local host (127.0.0.1).
# The web server must be available only at http://127.0.0.1:8080.
#
# Requirements:
# • The container must be started with the Nginx web server installed.
# • Container port 80 must be published to host port 8080.
# • Access to the web server must be restricted only to the local host (127.0.0.1).
# • The web server must be available at http://127.0.0.1:8080.
# • External access to port 8080 must be blocked for all IP addresses except 127.0.0.1.
#
# ## 🇺🇦 Ukrainian version:
#
# Публікація портів з обмеженням по IP
# Запустіть контейнер з Nginx, опублікуйте порт 80 контейнера на порт 8080 хоста,
# але обмежте доступ тільки для локального хоста (127.0.0.1).
# Веб-сервер повинен бути доступний тільки за адресою http://127.0.0.1:8080.
#
# Вимоги:
# • Контейнер повинен бути запущений з встановленим веб-сервером Nginx.
# • Порт 80 контейнера повинен бути опублікований на порт 8080 хоста.
# • Доступ до веб-сервера повинен бути обмежений тільки для локального хоста (127.0.0.1).
# • Веб-сервер повинен бути доступний за адресою http://127.0.0.1:8080.
# • Зовнішній доступ до порту 8080 повинен бути заблокований для всіх IP, окрім 127.0.0.1.

# Running a container with IP restriction
docker run -d -p 127.0.0.1:8080:80 nginx:latest