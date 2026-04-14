# Mounting a Bind Directory
# Run a container based on the nginx image, mounting the /host/project directory
# on the host into the /app directory inside the container.
# Name the container project_container.
#
# Requirements:
# • The container must be started based on the official nginx image.
# • The /host/project directory on the host must be mounted into the /app directory inside the container.
# • The container must be named project_container.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування прив'язаної директорії
# Запустіть контейнер на основі образу nginx, змонтувавши директорію /host/project на хості
# в директорію /app всередині контейнера.
# Назвіть контейнер project_container.
#
# Вимоги:
# • Контейнер має бути запущений на основі офіційного образу nginx.
# • Директорія /host/project на хості має бути змонтована в директорію /app всередині контейнера.
# • Контейнер має бути названий project_container.

# Run a container based on the nginx image, mounting the /host/project directory
# on the host into the /app directory inside the container
docker run -d -v /host/project:/app --name project_container nginx