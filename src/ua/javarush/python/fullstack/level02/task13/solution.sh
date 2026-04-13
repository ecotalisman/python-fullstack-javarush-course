# Viewing Logs in Real Time
# Follow log updates in real time for the container named db_service.
# Use a command that displays new log entries as they appear.
#
# Requirements:
# • A command must be used to monitor the logs of the container named db_service in real time.
# • The command must display new log entries as they appear, without delays.
# • The command must explicitly specify the container name db_service to retrieve its logs.
#
# ## 🇺🇦 Ukrainian version:
#
# Перегляд логів у реальному часі
# Слідкуйте за оновленнями логів у реальному часі для контейнера з ім'ям db_service.
# Використовуйте команду, яка буде відображати нові записи у логах у міру їх появи.
#
# Вимоги:
# • Необхідно використовувати команду для моніторингу логів контейнера з ім'ям db_service у реальному часі.
# • Команда має відображати нові записи у логах у міру їх появи, без затримок.
# • Команда має явно вказувати ім'я контейнера db_service для отримання його логів.

# Command for monitoring the logs of the container named db_service in real time
docker logs -f db_service