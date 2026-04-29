# Mounting Multiple Volumes
# Create two volumes, data_volume and logs_volume.
# Run a container with Nginx, mounting data_volume into the /data directory
# and logs_volume into the /logs directory.
#
# Requirements:
# • Two volumes named data_volume and logs_volume must be created.
# • The Nginx container must mount the data_volume volume into the /data directory inside the container.
# • The Nginx container must mount the logs_volume volume into the /logs directory inside the container.
# • The running container must contain an installed Nginx server.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування декількох томів
# Створіть два томи data_volume і logs_volume.
# Запустіть контейнер з Nginx, змонтувавши data_volume у директорію /data
# і logs_volume у директорію /logs.
#
# Вимоги:
# • Мають бути створені два томи з іменами data_volume і logs_volume.
# • Контейнер з Nginx повинен монтувати том data_volume у директорію /data всередині контейнера.
# • Контейнер з Nginx повинен монтувати том logs_volume у директорію /logs всередині контейнера.
# • Запущений контейнер повинен містити встановлений сервер Nginx.

# Create two volumes: data_volume and logs_volume
docker volume create data_volume && docker volume create logs_volume

# Run a container with Nginx, mounting data_volume into the /data directory
# and logs_volume into the /logs directory
docker run -d --name app -v data_volume:/data -v logs_volume:/logs nginx