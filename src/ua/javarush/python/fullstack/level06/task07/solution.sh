# Cleaning Up Unused Volumes
# Create several volumes for different containers, then stop and remove the containers.
# Use the docker volume prune command to clean up all unused volumes.
#
# Requirements:
# • The script must create several volumes that will be used by different containers for data storage.
# • The script must include stopping the containers so that they no longer use the volumes.
# • After stopping the containers, the script must remove these containers, freeing the resources associated with them.
# • The script must use the docker volume prune command to remove all volumes that are no longer used by containers.
# • The script must confirm the successful removal of unused volumes by displaying an appropriate message to the user.
#
# ## 🇺🇦 Ukrainian version:
#
# Очищення невикористовуваних томів
# Створіть кілька томів для різних контейнерів, а потім зупиніть і видаліть контейнери.
# Використовуйте команду docker volume prune для очищення всіх невикористовуваних томів.
#
# Вимоги:
# • Скрипт повинен створити кілька томів, які будуть використовуватися різними контейнерами для зберігання даних.
# • Скрипт повинен передбачати зупинку контейнерів, щоб вони більше не використовували томи.
# • Після зупинки контейнерів, скрипт повинен видалити ці контейнери, звільняючи пов’язані з ними ресурси.
# • Скрипт повинен використовувати команду docker volume prune для видалення всіх томів, які більше не використовуються контейнерами.
# • Скрипт повинен підтвердити успішне видалення невикористовуваних томів, надаючи користувачу відповідне повідомлення.

# Creating several volumes
docker volume create front_volume
docker volume create back_volume

# Creating and starting containers that use these volumes
docker run -d --name webserver -v front_volume:/usr/share/nginx/html nginx
docker run -d --name app -v back_volume:/var/log/app busybox sleep 1000

# Stopping the containers
docker stop webserver app

# Removing the containers
docker rm webserver app

# Confirming volume removal
if docker volume prune -f; then
  echo "Unused volumes have been successfully removed."
else
  echo "Error during volume cleanup"
fi