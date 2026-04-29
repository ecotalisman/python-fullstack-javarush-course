# Removing a Volume
# Create a volume named logs_volume and run a container using this volume.
# After stopping and removing the container, remove the volume.
# Check that the volume no longer exists using the docker volume ls command.
#
# Requirements:
# • A Docker volume named logs_volume must be created before starting the container.
# • The container must be started using the created logs_volume volume.
# • After stopping the container, it must be completely removed.
# • After removing the container, the logs_volume volume must be removed.
# • The docker volume ls command must be used to check that the logs_volume volume no longer exists.
#
# ## 🇺🇦 Ukrainian version:
#
# Видалення тому
# Створіть том із назвою logs_volume та запустіть контейнер із використанням цього тому.
# Після зупинки та видалення контейнера, видаліть том.
# Перевірте, що тому більше не існує за допомогою команди docker volume ls.
#
# Вимоги:
# • Необхідно створити Docker том із назвою logs_volume перед запуском контейнера.
# • Контейнер має бути запущений із використанням створеного тому logs_volume.
# • Після зупинки контейнера його необхідно повністю видалити.
# • Після видалення контейнера необхідно видалити том logs_volume.
# • Необхідно використати команду docker volume ls для перевірки відсутності тому logs_volume.

# Create a volume named logs_volume for storing logs
docker volume create logs_volume

# Run a container, for example Nginx, mounting the logs_volume volume
docker run -d --name webserver -v logs_volume:/usr/share/nginx/html nginx

# Stop the container
docker stop webserver

# Remove the container
docker rm webserver

# Remove the logs_volume volume
docker volume rm logs_volume

# Check that the volume no longer exists
docker volume ls