# Downloading and Running an Image from Docker Hub
# Download the nginx:latest image from Docker Hub and run a container from it. Map container port 80 to port 8080 on your local machine.
#
# Requirements:
# • The script must download the nginx image with the latest tag from Docker Hub.
# • The script must run a container based on the downloaded nginx:latest image.
# • The script must map container port 80 to port 8080 on the local machine.
# • Standard Docker commands must be used to download the image and run the container.
#
# ## 🇺🇦 Ukrainian version:
# Завантаження та запуск образу з Docker Hub
# Завантажте з Docker Hub образ nginx:latest та запустіть контейнер з ним. Перенаправте порт 80 контейнера на порт 8080 вашої локальної машини.
#
# Вимоги:
# • Скрипт повинен завантажувати образ nginx з тегом latest з Docker Hub.
# • Скрипт повинен запускати контейнер на основі завантаженого образу nginx:latest.
# • Скрипт повинен перенаправляти порт 80 контейнера на порт 8080 локальної машини.
# • Для завантаження образу та запуску контейнера повинні використовуватися стандартні команди Docker.

# Downloading the nginx:latest image from Docker Hub
docker pull nginx:latest

# Running the container with container port 80 mapped to port 8080 on the local machine
docker run -d -p 8080:80 nginx:latest
