# Running a Container on the bridge Network
# Create a container with Nginx and connect it to the default Docker network (bridge).
# Configure port forwarding from host port 8080 to container port 80
# so that the web server is available at localhost:8080.
#
# Requirements:
# • The container must be created using the Nginx image.
# • The container must be connected to the default Docker network (bridge) provided by Docker.
# • Host port 8080 must be forwarded to container port 80 to provide access to the web server through localhost:8080.
# • After configuration, the Nginx web server must be accessible in a browser at http://localhost:8080.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск контейнера в bridge-мережі
# Створіть контейнер з Nginx і підключіть його до мережі за замовчуванням (bridge).
# Налаштуйте перенаправлення порту 8080 на 80 порт контейнера,
# щоб веб-сервер був доступний за адресою localhost:8080.
#
# Вимоги:
# • Контейнер має бути створений із використанням образу Nginx.
# • Контейнер має бути підключений до мережі за замовчуванням (bridge), наданої Docker.
# • Порт 8080 хоста має бути перенаправлений на порт 80 контейнера, щоб забезпечити доступ до веб-сервера через localhost:8080.
# • Після налаштування веб-сервер Nginx має бути доступний через браузер за адресою http://localhost:8080.

# Running a Docker container with Nginx
docker run -d -p 8080:80 nginx