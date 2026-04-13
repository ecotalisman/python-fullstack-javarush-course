# Viewing the Contents of a Directory
# Run a command that displays the contents of the /var/log directory inside the container
# named my_app_container. Use the docker exec command.
#
# Requirements:
# • The docker exec command must be used to run a command inside a running container.
# • The command must include the container name my_app_container in which the action will be performed.
# • The command must display the contents of the /var/log directory inside the specified container.
#
# ## 🇺🇦 Ukrainian version:
#
# Перегляд вмісту директорії
# Виконайте команду, яка відобразить вміст директорії /var/log всередині контейнера
# з ім'ям my_app_container. Використовуйте команду docker exec.
#
# Вимоги:
# • Необхідно використовувати команду docker exec для виконання команди всередині запущеного контейнера.
# • Команда повинна містити ім'я контейнера my_app_container, в якому буде виконано дію.
# • Команда повинна відобразити вміст директорії /var/log всередині зазначеного контейнера.

# The command must display the contents of the /var/log directory inside the specified container.
docker exec my_app_container ls /var/log