# Restarting a Container with a Timeout
# Restart the container named cache_service, setting a timeout of 15 seconds before restarting it.
# Use the docker restart command.
#
# Requirements:
# • The docker restart command must be used to restart the container.
# • The name of the container to be restarted must be specified as cache_service.
# • A timeout of 15 seconds must be set before restarting the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Перезапуск контейнера з тайм-аутом
# Перезапустіть контейнер з іменем cache_service, встановивши тайм-аут у 15 секунд перед його перезапуском.
# Використовуйте команду docker restart.
#
# Вимоги:
# • Для перезапуску контейнера необхідно використовувати команду docker restart.
# • Ім'я контейнера, який необхідно перезапустити, має бути вказане як cache_service.
# • Перед перезапуском контейнера необхідно встановити тайм-аут у 15 секунд.

# Restarting the cache_service container with a timeout of 15 seconds
docker restart -t 15 cache_service