# Mounting a Volume into a Container
# Create a volume named app_data and run a container with Nginx,
# mounting this volume into the /app directory inside the container.
#
# Requirements:
# • A volume named app_data must be created and used for mounting into the container.
# • A Docker container with Nginx installed and running must be started.
# • The app_data volume must be mounted into the /app directory
#   inside the running Nginx container.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування тому в контейнер
# Створіть том із назвою app_data та запустіть контейнер із Nginx,
# монтувавши цей том у директорію /app всередині контейнера.
#
# Вимоги:
# • Повинен бути створений том із назвою app_data, який буде використовуватися для монтування в контейнер.
# • Необхідно запустити Docker-контейнер, у якому буде встановлений і запущений Nginx.
# • Том app_data повинен бути змонтований у директорію /app всередині запущеного контейнера з Nginx.

# Create a volume
docker volume create app_data

# Run a container with Nginx, mounting the app_data volume
# into the /app directory inside the container
docker run -d --name web -v app_data:/app nginx