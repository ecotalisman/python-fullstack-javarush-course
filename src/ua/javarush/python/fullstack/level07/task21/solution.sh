# Logs for a Specific Period
# Output the logs of the database_container container for the period from July 1, 2023 to July 2, 2023,
# using the --since and --until options of the docker logs command.
#
# Requirements:
# • The docker logs command must be used to output the container logs.
# • The command must use the container name database_container to retrieve its logs.
# • The --since option with the date July 1, 2023 must be used to specify the start of the log period.
# • The --until option with the date July 2, 2023 must be used to specify the end of the log period.
#
# 🇺🇦 Ukrainian version:
#
# Логи за певний період
# Виведіть логи контейнера database_container за період з 1 липня 2023 року до 2 липня 2023 року, використовуючи параметри --since і --until команди docker logs.
#
# Вимоги:
# • Для виведення логів контейнера необхідно використовувати команду docker logs.
# • Команда повинна використовувати ім'я контейнера database_container для отримання логів.
# • Необхідно використовувати параметр --since з датою 1 липня 2023 року для зазначення початку періоду логів.
# • Необхідно використовувати параметр --until з датою 2 липня 2023 року для зазначення закінчення періоду логів.

# Logs of the database_container container for the period from July 1, 2023 to July 2, 2023
docker logs --since "2023-07-01" --until "2023-07-02" database_container