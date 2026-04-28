# Monitoring Container Activity
# Start a container and enable monitoring of its activity using the docker events command.
# Monitor all events that occur with the container.
#
# Requirements:
# • A container must be started using the appropriate Docker command.
# • The docker events command must be used to monitor container activity.
# • The script must track all events that occur with the container, without exceptions.
# • Monitoring must be configured so that event tracking continues for a specified time
#   or until it is stopped manually.
# • Each event that occurs with the container must be displayed in the terminal or log.
#
# ## 🇺🇦 Ukrainian version:
#
# Моніторинг активності контейнера
# Запустіть контейнер та увімкніть моніторинг його активності за допомогою команди docker events.
# Моніторте всі події, що відбуваються з контейнером.
#
# Вимоги:
# • Необхідно запустити контейнер за допомогою відповідної команди Docker.
# • Необхідно використовувати команду docker events для моніторингу активності контейнера.
# • Скрипт має відстежувати всі події, що відбуваються з контейнером, без виключень.
# • Моніторинг має бути налаштований таким чином, щоб продовжувати відстеження подій протягом заданого часу або до ручної зупинки.
# • Кожна подія, що відбувається з контейнером, має бути відображена у терміналі або журналі.

# Start a container with Nginx
docker run -d --name monitored_nginx nginx

# Enable container activity monitoring using the docker events command
# Monitor all events that occur with the monitored_nginx container
sleep 2
timeout 10 docker events --filter container=monitored_nginx