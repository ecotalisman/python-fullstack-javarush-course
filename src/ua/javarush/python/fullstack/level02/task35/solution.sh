# Running the Nginx Web Server
# After downloading the Nginx image, run a container with the Nginx web server,
# forwarding container port 80 to port 8080 on the host machine.
# The container must run in detached mode. Name it nginx_server.
#
# Requirements:
# • The Nginx image must be downloaded from Docker Hub before starting the container.
# • The container must be started with port forwarding from container port 80 to port 8080 on the host machine.
# • The container must be started in detached mode.
# • The container must be named nginx_server when started.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск веб-сервера Nginx
# Після завантаження образу Nginx, запустіть контейнер із веб-сервером Nginx,
# перенаправивши порт 80 контейнера на порт 8080 хост-машини.
# Контейнер має працювати у фоновому режимі. Назвіть його nginx_server.
#
# Вимоги:
# • Потрібно завантажити образ Nginx із Docker Hub перед запуском контейнера.
# • Контейнер має запускатися з перенаправленням порту 80 контейнера на порт 8080 хост-машини.
# • Контейнер має бути запущений у фоновому режимі (detached mode).
# • Контейнер має бути названий nginx_server при запуску.

# Downloading the Nginx image from Docker Hub
docker pull nginx

# Running the Nginx container in detached mode with port forwarding
docker run -d -p 8080:80 --name nginx_server nginx