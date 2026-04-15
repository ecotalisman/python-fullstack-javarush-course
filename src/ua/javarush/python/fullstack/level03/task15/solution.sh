# Building an Image Without Using Cache
# Create a Dockerfile for a Python application that copies the code into the container
# and installs dependencies. Build an image named my_python_app without using cache.
#
# Requirements:
# • A Dockerfile must be created and include instructions for copying the Python application code
#   into the container and installing the required dependencies.
# • The Dockerfile must contain a COPY or ADD instruction to copy the Python application code
#   into the container.
# • The Dockerfile must include a command to install all required Python application dependencies,
#   such as using a RUN instruction to install libraries from the requirements.txt file.
# • The image must be built with the name my_python_app, specified using the -t flag
#   in the docker build command.
# • The image must be built without using cache, which is ensured by adding the --no-cache flag
#   to the docker build command.
#
# ## 🇺🇦 Ukrainian version:
#
# Збірка образу без використання кешу
# Створіть Dockerfile для Python-додатка, який копіює код у контейнер та встановлює залежності.
# Зберіть образ із назвою my_python_app без використання кешу.
#
# Вимоги:
# • Dockerfile має бути створений та включати інструкції для копіювання коду Python-додатка у контейнер
#   і встановлення необхідних залежностей.
# • Dockerfile має містити команду COPY або ADD, за допомогою якої код Python-додатка копіюється у контейнер.
# • Dockerfile повинен включати команду для встановлення всіх необхідних залежностей Python-додатка,
#   таких як використання інструкції RUN для встановлення бібліотек із файлу requirements.txt.
# • Образ має бути зібраний із назвою my_python_app, що вказується за допомогою прапора -t
#   у команді docker build.
# • Образ має бути зібраний без використання кешу, що забезпечується додаванням прапора --no-cache
#   у команду docker build.

# Building without using cache:
docker build -t my_python_app --no-cache .