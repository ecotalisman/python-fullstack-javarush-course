# Running Multiple Containers
# Start two containers named web_server and db_server at the same time.
# Use the docker start command.
#
# Requirements:
# • The script must include a command to start the container named web_server using the docker start command.
# • The script must include a command to start the container named db_server using the docker start command.
# • The script must ensure that both containers (web_server and db_server) are started at the same time, without
# using sequential start commands.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск декількох контейнерів
# Запустіть два контейнери з іменами web_server і db_server одночасно.
# Використовуйте команду docker start.
#
# Вимоги:
# • Скрипт має включати команду для запуску контейнера з іменем web_server, використовуючи команду docker start.
# • Скрипт має включати команду для запуску контейнера з іменем db_server, використовуючи команду docker start.
# • Скрипт має забезпечити запуск обох контейнерів (web_server і db_server) одночасно, без використання послідовних
# команд запуску.

# Starting both containers at the same time
docker start web_server db_server