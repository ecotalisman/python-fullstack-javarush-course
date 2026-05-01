# Using Docker Secrets for a Database
# Create a secret for the database password using Docker Secrets
# and configure the PostgreSQL service to use this secret.
#
# Requirements:
# • Create a secret using Docker Secrets that will contain the password
#   for the PostgreSQL database.
# • Configure the PostgreSQL service so that it receives the password
#   from the created secret, not from environment variables or configuration files.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання Docker Secrets для бази даних
# Створіть секрет для пароля бази даних за допомогою Docker Secrets
# і налаштуйте сервіс PostgreSQL для використання цього секрету.
#
# Вимоги:
# • За допомогою Docker Secrets створіть секрет, який міститиме пароль
#   для бази даних PostgreSQL.
# • Налаштуйте сервіс PostgreSQL таким чином, щоб він отримував пароль
#   із створеного секрету, а не з змінних середовища або конфігураційних файлів.

# Create a secret for the PostgreSQL database password
printf "%s" "$DB_PASS" | docker secret create db_password -

# Create a network for the PostgreSQL service if it has not been created yet
docker network create postgres_network

# Create a PostgreSQL service using the password secret
docker service create --name postgres \
  --network postgres_network \
  --secret db_password \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/db_password \
  postgres