# Publishing a Single Port
# Run a container with Nginx and publish container port 80
# to host port 8080 so that the web server is available
# at http://localhost:8080.
#
# Requirements:
# • The Nginx container must be started with internal port 80 published.
# • External port 8080 on the host must be mapped to container port 80.
# • After starting the container, the Nginx web server must be available at http://localhost:8080.
#
# ## 🇺🇦 Ukrainian version:
#
# Публікація одного порту
# Запустіть контейнер з Nginx та опублікуйте порт 80 контейнера на порт 8080 хоста,
# щоб веб-сервер був доступний за адресою http://localhost:8080.
#
# Вимоги:
# • Контейнер Nginx має бути запущений з публікацією внутрішнього порту 80.
# • Зовнішній порт 8080 на хості має бути пов'язаний з портом 80 контейнера.
# • Після запуску контейнера веб-сервер Nginx має бути доступний за адресою http://localhost:8080.

# Running a container with port forwarding
docker run -d -p 8080:80 nginx