# Creating a Volume for Data Storage
# Create a volume named my_data_volume and run a container with Nginx,
# mounting this volume into the /data directory inside the container.
# The container must use this volume for data storage.
#
# Requirements:
# • A Docker volume named my_data_volume must be created
#   and used for storing container data.
# • A container with Nginx installed must be started
#   to serve as a web server.
# • The my_data_volume volume must be mounted into the /data directory
#   inside the Nginx container, allowing the container to use it for data storage.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення тому для зберігання даних
# Створіть том з ім'ям my_data_volume і запустіть контейнер з Nginx,
# змонтувавши цей том у директорію /data контейнера.
# Контейнер має використовувати цей том для зберігання даних.
#
# Вимоги:
# • У Docker необхідно створити том з ім'ям my_data_volume,
#   який буде використовуватись для зберігання даних контейнера.
# • Необхідно запустити контейнер з встановленим Nginx,
#   який буде обслуговувати веб-сервер.
# • Том my_data_volume має бути змонтований у директорію /data всередині контейнера Nginx,
#   дозволяючи контейнеру використовувати її для зберігання даних.

# Create a volume named my_data_volume
docker volume create my_data_volume

# Run a container with Nginx, mounting the my_data_volume volume
# into the /data directory inside the container
docker run -d --name my_nginx_container -v my_data_volume:/data nginx

# Check that the volume is attached to the container
docker volume ls

# Check that the volume was created
docker volume inspect my_data_volume