# Using Semantic Versioning
# Create a Dockerfile for an application using semantic versioning when building the image (for example, myapp:1.2.3). Run the container — the version must be displayed during the application's execution.
#
# Requirements:
# • The Dockerfile must be created for the specified application, allowing the container image to be built.
# • The application image must be built using semantic versioning, for example, myapp:1.2.3.
# • After the container is started, the application version must be displayed during its execution.
# • The container must be successfully started from the built image.
#
# ## 🇺🇦 Ukrainian version:
# Використання семантичного версіонування
# Створіть Dockerfile для додатка, використовуючи семантичне версіонування під час збірки образу (наприклад, myapp:1.2.3). Запустіть контейнер - версія повинна відображатися під час виконання додатка.
#
# Вимоги:
# • Dockerfile має бути створений для зазначеного додатка, що дозволить зібрати образ контейнера.
# • Образ додатка має бути зібраний з використанням семантичного версіонування, наприклад, myapp:1.2.3.
# • Після запуску контейнера версія додатка повинна відображатися під час його виконання.
# • Контейнер має бути успішно запущений зі зібраного образу.

# Build the Docker image with the specified version:
docker build -t myapp:1.2.3 .

# Run the container from the built image:
docker run myapp:1.2.3