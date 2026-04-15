# Using the FROM Instruction
# Create a Dockerfile that uses the python:3.9 base image.
# Add a command to run a Python application that outputs "Hello, Docker!".
# Build an image named my_python_app and run a container.
#
# Requirements:
# • The Dockerfile must contain the FROM instruction specifying the python:3.9 base image.
# • The Dockerfile must include a CMD or ENTRYPOINT command that runs a Python application that outputs "Hello, Docker!".
# • A Docker image named my_python_app must be built from the created Dockerfile.
# • A container must be run from the built my_python_app image.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання інструкції FROM
# Створіть Dockerfile, який використовує базовий образ python:3.9.
# Додайте команду для запуску Python-додатку, який виводить "Hello, Docker!".
# Зберіть образ із назвою my_python_app та запустіть контейнер.
#
# Вимоги:
# • Dockerfile має містити інструкцію FROM із зазначенням базового образу python:3.9.
# • Dockerfile має включати команду CMD або ENTRYPOINT, яка запускає Python-додаток, що виводить "Hello, Docker!".
# • Необхідно зібрати образ Docker із створеного Dockerfile з назвою my_python_app.
# • Контейнер має бути запущений із зібраного образу my_python_app.

# Building the image
docker build -t my_python_app .

# Running the container
docker run --name my_python_app my_python_app