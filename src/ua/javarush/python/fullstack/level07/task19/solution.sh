# Following Logs in Real Time
# Using the docker logs command, configure real-time log monitoring for the my_service container
# to track any new events.
#
# Requirements:
# • The docker logs command must be used to monitor the logs of the my_service container.
# • Monitoring must be configured to track new events occurring in the container in real time.
# • The docker logs command must be applied to the specific container named my_service.
# • Logs must update automatically to display all new events without the need to enter the command again.
#
# 🇺🇦 Ukrainian version:
#
# Відстеження логів у реальному часі
# Використовуючи команду docker logs, налаштуйте моніторинг логів контейнера my_service у реальному часі, щоб відстежувати будь-які нові події.
#
# Вимоги:
# • Для моніторингу логів контейнера my_service необхідно використовувати команду docker logs.
# • Моніторинг має бути налаштований так, щоб у реальному часі відстежувати нові події, що відбуваються у контейнері.
# • Команда docker logs має бути застосована до конкретного контейнера з ім'ям my_service.
# • Логи повинні автоматично оновлюватися для відображення всіх нових подій без необхідності повторного введення команди.

# Running a container with the name my_service
docker run -d --name my_service nginx

# Using the docker logs command with the -f flag to follow logs in real time
docker logs -f my_service