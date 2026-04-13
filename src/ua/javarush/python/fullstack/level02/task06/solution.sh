# Stopping a Container with a Timeout
# Stop the container named app_container, setting a timeout of 30 seconds
# for the container to shut down gracefully.
#
# Requirements:
# • The docker stop command must be used to stop the container.
# • The docker stop command must specify the container name app_container.
# • The docker stop command must include a parameter to set the container shutdown timeout to 30 seconds.
#
# ## 🇺🇦 Ukrainian version:
#
# Зупинка контейнера з тайм-аутом
# Зупиніть контейнер з іменем app_container, встановивши тайм-аут для коректного завершення роботи контейнера в 30 секунд.
#
# Вимоги:
# • Для зупинки контейнера необхідно використовувати команду docker stop.
# • У команді docker stop має бути вказане ім'я контейнера, яке дорівнює app_container.
# • Команда docker stop повинна включати параметр для встановлення тайм-ауту завершення роботи контейнера, рівного 30 секунд.

# Stopping the container named app_container with a timeout of 30 seconds
docker stop -t 30 app_container