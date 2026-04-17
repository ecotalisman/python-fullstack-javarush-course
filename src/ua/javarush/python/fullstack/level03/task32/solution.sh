# Assigning Tags for Development and Production Environments
# Create a Dockerfile for your application, build two images with the tags myapp:dev for development and myapp:prod for production. Different environment variables must be configured inside the containers for these versions.
#
# Requirements:
# • The Dockerfile must be created for your application to be used in the image build process.
# • It is necessary to build two Docker images with different tags: myapp:dev for the development environment and myapp:prod for production.
# • Inside the containers built from the myapp:dev and myapp:prod images, different environment variables must be configured according to their purpose.
#
# ## 🇺🇦 Ukrainian version:
# Присвоєння тегу для середовищ розробки та продакшн
# Створіть Dockerfile для вашого додатка, зберіть два образи з тегами: myapp:dev для розробки та myapp:prod для продакшн. Всередині контейнерів повинні бути налаштовані різні змінні середовища для цих версій.
#
# Вимоги:
# • Dockerfile має бути створено для вашого додатка, щоб використовуватися в процесі збірки образів.
# • Необхідно зібрати два Docker-образи з різними тегами: myapp:dev для середовища розробки та myapp:prod для продакшн.
# • Всередині контейнерів, зібраних із образів myapp:dev та myapp:prod, повинні бути налаштовані різні змінні середовища, що відповідають їхньому призначенню.

# Building and running the image for development
docker build --build-arg ENVIRONMENT=development -t myapp:dev .
docker run myapp:dev

# Building and running the image for production
docker build --build-arg ENVIRONMENT=production -t myapp:prod .
docker run myapp:prod