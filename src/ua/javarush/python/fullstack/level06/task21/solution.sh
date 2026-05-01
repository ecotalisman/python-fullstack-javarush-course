# Creating a Secret for the Database
# Create a secret for the PostgreSQL database password.
# Use this secret when creating the PostgreSQL service
# to pass the password through a secure file.
#
# Requirements:
# • The script must include creating a secret containing the PostgreSQL database password
#   using the Docker utility.
# • When creating the PostgreSQL service, the previously created secret must be used
#   to pass the database password through a secure file.
# • The PostgreSQL database password must be passed only through secure methods,
#   using a Docker secret, without including the password in plain text
#   in the configuration or code.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення секрету для бази даних
# Створіть секрет для пароля бази даних PostgreSQL.
# Використовуйте цей секрет при створенні сервісу PostgreSQL,
# щоб передати пароль через безпечний файл.
#
# Вимоги:
# • Скрипт має включати створення секрету, що містить пароль бази даних PostgreSQL,
#   з використанням утиліти Docker.
# • При створенні сервісу PostgreSQL потрібно використовувати раніше створений секрет,
#   щоб передати пароль для бази даних через безпечний файл.
# • Пароль для бази даних PostgreSQL має передаватися лише через безпечні методи,
#   використовуючи Docker-секрет, без включення пароля у відкритому вигляді
#   у конфігурації або коді.

# Creating a secret for the PostgreSQL database password
printf "%s" "$DB_PASS" | docker secret create db_password -

# Creating a PostgreSQL service using the created secret
docker service create --name postgres --secret db_password -e POSTGRES_PASSWORD_FILE=/run/secrets/db_password postgres