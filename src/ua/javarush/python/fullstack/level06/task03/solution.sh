# Storing Database Data in a Volume
# Create a volume for storing PostgreSQL data named pg_data.
# Run a PostgreSQL container using this volume to store data
# in the /var/lib/postgresql/data directory inside the container.
# The data must persist between container restarts.
#
# Requirements:
# • A Docker volume named pg_data must be created for storing PostgreSQL data.
# • The pg_data volume must be mounted into the container at the path /var/lib/postgresql/data.
# • Start a PostgreSQL container using the previously created volume for data storage.
# • The data in the volume must persist between container restarts, ensuring its durability.
#
# ## 🇺🇦 Ukrainian version:
#
# Збереження даних бази даних в томі
# Створіть том для зберігання даних PostgreSQL з іменем pg_data.
# Запустіть контейнер з PostgreSQL, використовуючи цей том для зберігання даних
# у директорії /var/lib/postgresql/data контейнера.
# Дані повинні зберігатись між перезапусками контейнера.
#
# Вимоги:
# • Необхідно створити Docker-том з іменем pg_data для зберігання даних PostgreSQL.
# • Том pg_data повинен бути змонтований у контейнері за шляхом /var/lib/postgresql/data.
# • Запустіть контейнер з PostgreSQL, використовуючи раніше створений том для зберігання даних.
# • Дані у томі повинні зберігатись між перезапусками контейнера, забезпечуючи їх сталість.

# Create a volume named pg_data for storing PostgreSQL data
docker volume create pg_data

# Run a PostgreSQL container, mounting the pg_data volume
# into the /var/lib/postgresql/data directory inside the container
docker run -d --name db -v pg_data:/var/lib/postgresql/data postgresql