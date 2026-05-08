# Formatted Output of Metrics Using docker stats
# Use the docker stats command with the --format option
# to output only the container name, CPU usage percentage, and memory usage percentage.
# Present the data in a table.
#
# Requirements:
# • The script must use the docker stats command with the --format flag
#   to output container metrics.
# • The script must output only the container name,
#   CPU usage percentage, and memory usage percentage.
# • The output data must be presented in a table format
#   to ensure clarity and structured information.
#
# ## 🇺🇦 Ukrainian version:
#
# Форматований вивід метрик з використанням docker stats
# Використайте команду docker stats з параметром --format,
# щоб вивести тільки ім'я контейнера, відсоток використання CPU та пам'яті.
# Представте дані в таблиці.
#
# Вимоги:
# • Скрипт повинен використовувати команду docker stats з флагом --format
#   для виводу метрик контейнерів.
# • Скрипт повинен виводити тільки ім'я контейнера,
#   відсоток використання CPU та відсоток використання пам'яті.
# • Виведені дані повинні бути представлені у табличному форматі,
#   щоб забезпечити зрозумілість і структурованість інформації.

# Starting a container with Nginx
docker run -d --name nginx_container -p 8080:80 nginx

# Starting a container with PostgreSQL
docker run -d --name postgres_container \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -p 5432:5432 \
    postgres

# Outputting the container name, CPU usage percentage, and memory usage percentage.
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemPerc}}"