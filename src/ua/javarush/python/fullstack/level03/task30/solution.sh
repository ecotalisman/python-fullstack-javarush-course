# Assigning Multiple Image Tags
# Build a Docker image for a Node.js application and assign it two tags: myapp:2.0 and myapp:latest. Both tags must work when running a container.
#
# Requirements:
# • The script must build a Docker image based on a Dockerfile that defines the runtime environment for the Node.js application.
# • After the Docker image is built, it must be assigned the tag myapp:2.0, which allows running a container using this tag.
# • The Docker image must also be assigned an additional tag myapp:latest, which also allows running a container using this tag.
# • Both tags, myapp:2.0 and myapp:latest, must be functional, and the container must start correctly when using either of them.
#
# ## 🇺🇦 Ukrainian version:
# Присвоєння кількох тегів образу
# Зберіть Docker-образ для Node.js застосунку та присвойте йому два теги: myapp:2.0 і myapp:latest. Обидва теги повинні працювати при запуску контейнера.
#
# Вимоги:
# • Скрипт повинен збирати Docker-образ на основі Dockerfile, який визначає середовище виконання для Node.js застосунку.
# • Docker-образу після його збирання повинен бути присвоєний тег myapp:2.0, який дозволяє запускати контейнер із використанням цього тегу.
# • Docker-образу повинен бути присвоєний додатковий тег myapp:latest, який також дозволяє запускати контейнер із використанням цього тегу.
# • Обидва теги myapp:2.0 і myapp:latest повинні бути функціональними, і контейнер повинен коректно запускатись при використанні будь-якого з них.

# Building the Docker image with the tag myapp:2.0
docker build -t myapp:2.0 .

# Assigning the additional tag myapp:latest to the same image
docker tag myapp:2.0 myapp:latest

# Checking both tags
docker images