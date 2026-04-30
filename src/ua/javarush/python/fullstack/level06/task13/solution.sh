# Restoring Data into a Volume
# Restore data from the backup created in the previous task into the app_data volume
# and use this data in an Nginx container.
#
# Requirements:
# • A volume named app_data must be created and used for storing the restored data.
# • The data must be restored from the backup created in the previous task
#   and placed into the app_data volume.
# • The Nginx container must be configured to use the data restored
#   into the app_data volume for its operation.
#
# ## 🇺🇦 Ukrainian version:
#
# Відновлення даних у томі
# Відновіть дані з бекапу, створеного у попередньому завданні,
# у том app_data і використовуйте ці дані в контейнері Nginx.
#
# Вимоги:
# • Необхідно створити том з ім'ям app_data, який буде використовуватися для зберігання відновлених даних.
# • Дані мають бути відновлені з бекапу, створеного у попередньому завданні, і поміщені в том app_data.
# • Контейнер Nginx повинен бути налаштований на використання даних, відновлених у том app_data, для своєї роботи.

# It is assumed that you already have the app_data_backup.tar.gz backup file in the current directory

# Make sure that the volume named app_data exists; if not, create it
docker volume create app_data

# Restore data from the backup into the app_data volume
docker run --rm -v app_data:/data -v $(pwd):/backup busybox tar xzf /backup/app_data_backup.tar.gz -C /data

# Run a container with Nginx, mounting the restored app_data volume to use the data
docker run -d --name web -v app_data:/usr/share/nginx/html nginx

# Check that the container is running and that the data from the app_data volume is being used
docker inspect web