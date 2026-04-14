# Setting Memory Limits for a Container
# Create a container based on the nginx image, limiting its memory usage to 512 MB.
# Name the container memory_limited_container.
#
# Requirements:
# • The container must be created based on the official nginx image available on Docker Hub.
# • The container must have a memory usage limit set to 512 MB.
# • The container must be named memory_limited_container.
#
# ## 🇺🇦 Ukrainian version:
#
# Установка лімітів на пам'ять контейнера
# Створіть контейнер на основі образу nginx, обмеживши його використання пам'яті до 512 MB.
# Назвіть контейнер memory_limited_container.
#
# Вимоги:
# • Контейнер має бути створений на основі офіційного образу nginx, доступного на Docker Hub.
# • Контейнер повинен мати обмеження на використання пам'яті, встановлене на рівні 512 MB.
# • Контейнер повинен бути названий memory_limited_container.

# Create a container based on the nginx image, limiting its memory usage to 512 MB
docker run -d --name memory_limited_container --memory=512m nginx