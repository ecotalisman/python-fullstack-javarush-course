# Creating a Named Volume and Mounting It into a Container
# Create a named volume app_data and run a container based on the nginx image,
# mounting this volume into the /data directory inside the container.
# Name the container app_container.
#
# Requirements:
# • A named volume called app_data must be created and used for data storage.
# • A container must be started using the nginx image as its base.
# • The named volume app_data must be mounted into the /data directory inside the running container.
# • The container must be named app_container.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення іменованого тому та монтування в контейнер
# Створіть іменований том app_data та запустіть контейнер на основі образу nginx,
# змонтувавши цей том у директорію /data всередині контейнера.
# Назвіть контейнер app_container.
#
# Вимоги:
# • Необхідно створити іменований том з назвою app_data, який буде використовуватися для збереження даних.
# • Потрібно запустити контейнер, використовуючи образ nginx як основу для його роботи.
# • Іменований том app_data має бути змонтований у директорію /data всередині запущеного контейнера.
# • Контейнер має бути названий app_container.

# Create a named volume:
docker volume create app_data

# Run a container with the volume mounted:
docker run -d -v app_data:/data --name app_container nginx