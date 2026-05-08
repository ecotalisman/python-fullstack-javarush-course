# Monitoring with Metrics Output Once
# Start several containers and collect metrics for each container
# using the docker stats command with the --no-stream option
# to output metrics only once.
# Compare CPU and memory usage between containers
# and optimize resource consumption.
#
# Requirements:
# • The script must start several containers to make it possible
#   to collect metrics for each of them.
# • The script must use the docker stats command with the --no-stream option
#   to collect metrics so that they are collected only once
#   without repeated updates.
# • Visually compare CPU and memory usage metrics between containers
#   to determine the resource consumption level of each container.
# • Limit the amount of consumed resources based on the collected
#   and analyzed metrics:
#   1. Limit the MongoDB container memory to 512 MB.
#   2. Limit the Redis container to 50% of one CPU core.
#
# ## 🇺🇦 Ukrainian version:
#
# Моніторинг із виведенням метрик один раз
# Запустіть кілька контейнерів та зберіть метрики по кожному контейнеру,
# використовуючи команду docker stats з параметром --no-stream,
# щоб вивести метрики лише один раз.
# Порівняйте використання CPU та пам’яті між контейнерами
# та оптимізуйте споживання ресурсів.
#
# Вимоги:
# • Скрипт має запускати кілька контейнерів,
#   щоб забезпечити можливість збору метрик для кожного з них.
# • Скрипт має використовувати команду docker stats із параметром --no-stream
#   для збору метрик, щоб метрики були зібрані лише один раз
#   без повторного оновлення.
# • Візуально порівняйте метрики використання CPU та пам’яті між контейнерами,
#   щоб визначити рівень споживання ресурсів кожним контейнером.
# • Обмежте обсяги споживаних ресурсів,
#   базуючись на зібраних та проаналізованих метриках:
#   1. обмежте пам’ять контейнера MongoDB до 512 MB.
#   2. обмежте контейнер Redis до 50% одного ядра CPU.

# Starting several containers
docker run -d --name mongodb mongo
docker run -d --name redis-server redis

# Collecting metrics using docker stats
docker stats --no-stream

# Optimizing consumed resources
docker update mongodb --memory 512m 
docker update redis-server --cpus 0.5