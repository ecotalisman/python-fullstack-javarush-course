# Installing and Running cAdvisor
# Run cAdvisor in a Docker container to monitor your Docker containers.
# cAdvisor must be accessible through port 8080.
#
# Requirements:
# • cAdvisor must be running inside a Docker container.
# • cAdvisor must be configured to be accessible through port 8080.
# • cAdvisor must be configured to monitor all running Docker containers on the host.
#
# 🇺🇦 Ukrainian version:
#
# Встановлення та запуск cAdvisor
# Запустіть cAdvisor у Docker-контейнері для моніторингу ваших Docker-контейнерів.
# cAdvisor повинен бути доступним через порт 8080.
#
# Вимоги:
# • cAdvisor повинен бути запущений всередині Docker-контейнера.
# • cAdvisor повинен бути налаштований так, щоб бути доступним через порт 8080.
# • cAdvisor повинен бути налаштований для моніторингу всіх запущених Docker-контейнерів на хості.

# Running cAdvisor in a Docker container
docker run -d \
  --name=cadvisor \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --privileged \
  gcr.io/cadvisor/cadvisor:latest