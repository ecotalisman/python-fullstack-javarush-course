# Limiting the Number of Log Lines
# View the last 100 lines of logs for the container named api_service.
# This is needed to see only the most recent entries without reviewing the entire log.
#
# Requirements:
# • A Docker command must be used to view the logs of the container named api_service.
# • The command must be configured to display only the last 100 lines of the container logs.
# • The command must identify the container by its name api_service, not by ID or other characteristics.
#
# ## 🇺🇦 Ukrainian version:
#
# Обмеження кількості рядків логів
# Перегляньте останні 100 рядків логів для контейнера з іменем api_service.
# Це потрібно для того, щоб побачити тільки останні записи без необхідності переглядати увесь журнал логів.
#
# Вимоги:
# • Необхідно використовувати команду Docker для перегляду логів контейнера з іменем api_service.
# • Команда повинна бути налаштована таким чином, щоб відображати тільки останні 100 рядків логів контейнера.
# • Команда повинна ідентифікувати контейнер за його іменем api_service, а не за ідентифікатором чи іншими
# характеристиками.

# Showing the last 100 lines of logs for the container named api_service
docker logs -f --tail 100 api_service