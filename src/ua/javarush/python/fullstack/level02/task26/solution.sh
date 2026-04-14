# Port Forwarding with a Specified IP Address
# Run a container based on the nginx image, forwarding container port 80
# to port 8080 only on the 127.0.0.1 interface of the host machine.
# This will ensure that the service is accessible only from the local machine.
#
# Requirements:
# • The container must be started based on the official nginx image.
# • Port 80 inside the container must be forwarded to port 8080 on the host machine.
# • The port forwarding must include an IP address restriction so that the service is accessible
#   only through the 127.0.0.1 interface of the host machine.
#
# ## 🇺🇦 Ukrainian version:
#
# Перенаправлення порту із зазначенням IP-адреси
# Запустіть контейнер на основі образу nginx, перенаправивши порт 80 контейнера на порт 8080
# тільки на інтерфейсі 127.0.0.1 хост-машини. Це забезпечить доступ до сервісу лише з локальної машини.
#
# Вимоги:
# • Контейнер повинен бути запущений на основі офіційного образу nginx.
# • Порт 80 всередині контейнера повинен бути перенаправлений на порт 8080 хост-машини.
# • Перенаправлення порту повинно включати обмеження за IP-адресою, щоб доступ до сервісу був можливий
#   лише через інтерфейс 127.0.0.1 хост-машини.

# Run a container based on the nginx image, forwarding container port 80
# to port 8080 only on the 127.0.0.1 interface of the host machine
docker run -d -p 127.0.0.1:8080:80 nginx