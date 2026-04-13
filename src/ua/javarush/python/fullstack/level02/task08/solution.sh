# Removing a Container with Volumes
# Remove the stopped container named old_service and delete all volumes associated with it at the same time.
# Use the docker rm command.
#
# Requirements:
# • The docker rm command must be used to remove the container.
# • The container to be removed must have the exact name old_service, and this name must be specified in the command.
# • The docker rm command must include the option that removes all volumes associated with the old_service container.
#
# ## 🇺🇦 Ukrainian version:
#
# Видалення контейнера з томами
# Видаліть зупинений контейнер з іменем old_service, одночасно видаливши всі пов’язані з ним томи.
# Використовуйте команду docker rm.
#
# Вимоги:
# • Для видалення контейнера необхідно використовувати команду docker rm, щоб виконати це завдання.
# • Контейнер, який має бути видалений, має точну назву old_service і ця назва повинна бути вказана в команді.
# • Команда docker rm повинна включати опцію, яка виконує видалення всіх томів, пов’язаних із контейнером old_service.

# Removing a container with volumes
docker stop old_service
docker rm -v old_service