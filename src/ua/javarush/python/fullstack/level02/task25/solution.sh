# Multiple Port Forwarding
# Run a container based on the nginx image, forwarding container ports 80 and 443
# to host machine ports 8080 and 8443 respectively.
#
# Requirements:
# • The container must be started based on the official nginx image.
# • Container port 80 must be forwarded to port 8080 on the host machine.
# • Container port 443 must be forwarded to port 8443 on the host machine.
#
# ## 🇺🇦 Ukrainian version:
#
# Множинне перенаправлення портів
# Запустіть контейнер на основі образу nginx, перенаправивши порти 80 і 443 контейнера
# на порти 8080 і 8443 хост-машини відповідно.
#
# Вимоги:
# • Контейнер має бути запущений на основі офіційного образу nginx.
# • Порт 80 контейнера має бути перенаправлений на порт 8080 хост-машини.
# • Порт 443 контейнера має бути перенаправлений на порт 8443 хост-машини.

# Run a container based on the nginx image, forwarding container ports 80 and 443
# to host machine ports 8080 and 8443 respectively
docker run -d -p 8080:80 -p 8443:443 nginx