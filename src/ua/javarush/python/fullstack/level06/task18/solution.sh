# Mounting a Directory with the --mount Option
# Run a container using the --mount option, mounting the host directory /data
# into the /app directory inside the container with read-only permissions.
#
# Requirements:
# • The container must be started using the --mount option to mount a directory from the host.
# • The data source for mounting must point to the /data directory on the host.
# • The target directory for mounting inside the container must be /app.
# • The directory mounted into the container must have read-only permissions.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування директорії з параметром --mount
# Запустіть контейнер з використанням параметра --mount,
# змонтувавши директорію з хоста /data у контейнер в директорію /app
# з правами тільки для читання.
#
# Вимоги:
# • Контейнер повинен бути запущений з використанням параметра --mount для монтування директорії з хоста.
# • Джерело даних для монтування повинно вказувати на директорію /data на хості.
# • Цільова директорія для монтування в контейнері повинна бути /app.
# • Директорія, змонтована в контейнер, повинна мати права тільки для читання.

# Run a container, mounting a directory from the host into the container with read-only permissions
docker run -d --name app --mount type=bind,source=/data,target=/app,readonly nginx