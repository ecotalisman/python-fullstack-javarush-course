# Limiting the Number of Log Lines
# Display the last 15 lines of logs from the web_container container using the docker logs command.
# The output must include only the specified lines.
#
# Requirements:
# • The docker logs command must be used to display the container logs.
# • The command must be configured to display only the last 15 lines from the container logs.
# • The command must include the name of the web_container container to retrieve its logs.
#
# 🇺🇦 Ukrainian version:
#
# Обмеження кількості рядків логів
# Відобразьте останні 15 рядків логів контейнера web_container за допомогою команди docker logs. Вивід повинен включати тільки зазначені рядки.
#
# Вимоги:
# • Необхідно використовувати команду docker logs для відображення логів контейнера.
# • Команда повинна бути налаштована так, щоб відображати лише останні 15 рядків з логів контейнера.
# • Команда повинна містити вказівку імені контейнера web_container для отримання його логів.

# Display the last 15 lines of logs from the container named web_container
docker logs -f --tail 15 web_container