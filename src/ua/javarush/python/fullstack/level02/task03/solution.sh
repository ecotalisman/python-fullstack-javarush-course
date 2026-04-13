# Running a Container with an Environment Variable
# Run a container based on the Ubuntu image, passing the environment variable MY_VAR
# with the value HelloDocker. Inside the container, run the env command, which will display
# all environment variables.
#
# Requirements:
# • The script must use the Ubuntu image to run the container.
# • Setting an environment variable: The script must pass the environment variable MY_VAR
#   with the value HelloDocker to the container.
# • Running a command inside the container: Inside the container, the env command must be run
#   to display all environment variables.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск контейнера з змінною оточення
# Запустіть контейнер на основі образу ubuntu, передавши йому змінну оточення MY_VAR
# зі значенням HelloDocker. Всередині контейнера виконайте команду env, яка відобразить
# усі змінні оточення.
#
# Вимоги:
# • Скрипт повинен використовувати образ Ubuntu для запуску контейнера.
# • Встановлення змінної оточення: Скрипт повинен передати контейнеру змінну оточення MY_VAR
#   зі значенням HelloDocker.
# • Виконання команди всередині контейнера: Всередині контейнера повинна бути виконана команда env
#   для відображення усіх змінних оточення.

# Running a container with the Ubuntu image and passing an environment variable
docker run -e MY_VAR=HelloDocker ubuntu env