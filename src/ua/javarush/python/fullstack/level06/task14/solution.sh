# PostgreSQL Database Backup
# Start a PostgreSQL container, create a database,
# and perform a database backup using the pg_dump utility.
#
# Requirements:
# • A Docker container containing PostgreSQL must be created and started
#   with the appropriate settings for working with databases.
# • A new database must be created inside the running container
#   using PostgreSQL commands.
# • A backup of the created database must be performed using the pg_dump utility
#   to save the data to a file.
#
# ## 🇺🇦 Ukrainian version:
#
# Бекап бази даних PostgreSQL
# Запустіть контейнер з PostgreSQL, створіть базу даних
# і виконайте бекап бази даних за допомогою утиліти pg_dump.
#
# Вимоги:
# • Необхідно створити та запустити Docker-контейнер, що містить PostgreSQL,
#   з відповідними налаштуваннями для роботи з базами даних.
# • У запущеному контейнері має бути створена нова база даних за допомогою команд PostgreSQL.
# • Має бути виконаний бекап створеної бази даних за допомогою утиліти pg_dump
#   для збереження даних у файл.

# Start a PostgreSQL container, setting the password for the user
docker run -d --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword postgres

# Wait until PostgreSQL is fully started, a few seconds may be enough
sleep 10

# Create the database if it has not been created
# In this case, we have already specified it through an environment variable
docker exec -it postgres_container psql -U postgres -c "CREATE DATABASE mydatabase;"

# Create a table in the database for testing
docker exec -it postgres_container psql -U postgres -d mydatabase -c "CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));"

# Add test data to the table
docker exec -it postgres_container psql -U postgres -d mydatabase -c "INSERT INTO test_table (name) VALUES ('Test Entry 1'), ('Test Entry 2');"

# Perform a database backup using the pg_dump utility and save it on the host
docker exec -t postgres_container pg_dump -U postgres mydatabase > mydatabase_backup.sql

# Check that the backup was created
ls -l mydatabase_backup.sql