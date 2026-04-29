# Mounting a Volume with the --mount Option
# Create a volume named readonly_volume and run a container with Nginx,
# mounting the volume into the /app directory in read-only mode.
#
# Requirements:
# • A Docker volume named readonly_volume must be created before starting the Nginx container.
# • A container based on the Nginx image must be started using the --mount option to attach the volume.
# • The readonly_volume volume must be mounted into the container at the /app directory,
#   and access to it must be restricted to read-only mode.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування тому з параметром --mount
# Створіть том з іменем readonly_volume та запустіть контейнер із Nginx,
# монтувавши том у директорію /app в режимі "тільки для читання".
#
# Вимоги:
# • Необхідно створити том Docker з іменем readonly_volume перед запуском контейнера Nginx.
# • Слід запустити контейнер на основі образу Nginx, використовуючи параметр --mount для підключення тому.
# • Том readonly_volume має бути змонтованим у контейнер в директорію /app,
#   і доступ до нього має бути обмежений режимом "тільки для читання".

# Create a volume named readonly_volume
docker volume create readonly_volume

# Run a container with Nginx, mounting the readonly_volume volume
# into the /app directory in read-only mode
docker run -d --name web --mount source=readonly_volume,target=/app,readonly nginx