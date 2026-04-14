# Redirecting a Single Port
# Run a container based on the nginx image, forwarding container port 80
# to port 8080 on the host machine so that the Nginx web server is available
# at http://localhost:8080.
#
# Requirements:
# • The container must be created based on the official nginx image available on Docker Hub.
# • It is necessary to configure port forwarding from container port 80 to port 8080 on the host machine
#   to provide access to the Nginx web server via http://localhost:8080.
# • The container must be started in detached mode to ensure continuous access to the web server.
#
# ## 🇺🇦 Ukrainian version:
#
# Перенаправлення одного порту
# Запустіть контейнер на основі образу nginx, перенаправивши порт 80 контейнера на порт 8080 хост-машини,
# щоб вебсервер Nginx був доступний за адресою http://localhost:8080.
#
# Вимоги:
# • Контейнер має бути створений на основі офіційного образу nginx, доступного на Docker Hub.
# • Необхідно налаштувати перенаправлення порту 80 контейнера на порт 8080 хост-машини, щоб забезпечити доступ
#   до вебсервера Nginx через http://localhost:8080.
# • Контейнер має бути запущений у фоновому режимі, щоб забезпечувати постійний доступ до вебсервера.

# Run a container based on the nginx image, forwarding container port 80 to port 8080 on the host machine
docker run -d -p 8080:80 nginx