# Checking Volume Mounting
# Create a docker-compose.yml file with a PostgreSQL database and a volume for data storage.
# After starting the container, connect to it — the data must be successfully mounted in the volume.
#
# Requirements:
# • A docker-compose.yml file must be created, containing the configuration for running a PostgreSQL container.
# • The docker-compose.yml file must specify a volume that will be used to store PostgreSQL database data.
# • The docker-compose.yml file must configure a service for the PostgreSQL container using the appropriate base image.
# • The volume specified in docker-compose.yml must be correctly mounted in the PostgreSQL container for data storage.
# • After starting the container, it is necessary to verify that the database data is successfully stored in the specified volume.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка монтування томів
# Створіть файл docker-compose.yml з базою даних PostgreSQL і томом для збереження даних.
# Після запуску контейнера підключіться до нього - дані мають бути успішно змонтовані в том.
#
# Вимоги:
# • Необхідно створити файл docker-compose.yml, який міститиме конфігурацію для запуску контейнера з PostgreSQL.
# • У файлі docker-compose.yml має бути вказаний том, який використовуватиметься для збереження даних бази даних PostgreSQL.
# • У файлі docker-compose.yml має бути налаштована служба для контейнера з PostgreSQL, використовуючи відповідний базовий
# образ.
# • Том, вказаний у docker-compose.yml, має бути коректно змонтований у контейнері PostgreSQL для збереження даних.
# • Після запуску контейнера необхідно переконатися, що дані бази даних успішно зберігаються на вказаному томі.

# Starting the containers
docker compose up -d

# Pause to wait for the container to start
sleep 10

# Connecting and checking the data
docker exec -it postgres_container psql -U exampleuser -d exampledb -c "CREATE TABLE test (id SERIAL, name TEXT); INSERT INTO test (name) VALUES ('hello');"
docker compose down

docker compose up -d
sleep 10

docker exec -it postgres_container psql -U exampleuser -d exampledb -c "SELECT * FROM test;"

# Stopping the containers after verification
docker compose down