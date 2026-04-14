# Limiting CPU Usage for a Container
# Run a container based on the nginx image, limiting its CPU usage to no more than 1.5 CPUs.
# Name the container cpu_limited_container.
#
# Requirements:
# • The container must be started based on the official nginx image.
# • The container must be configured so that its CPU usage is limited to 1.5 CPUs.
# • The container must be named "cpu_limited_container".
#
# ## 🇺🇦 Ukrainian version:
#
# Обмеження використання CPU контейнером
# Запустіть контейнер на основі образу nginx, обмеживши його використання не більш ніж 1.5 CPU.
# Назвіть контейнер cpu_limited_container.
#
# Вимоги:
# • Контейнер повинен бути запущений на основі офіційного образу nginx.
# • Контейнер повинен бути налаштований так, щоб його використання процесора було обмежено до 1.5 CPU.
# • Контейнер повинен бути названий "cpu_limited_container".

# Run a container based on the nginx image, limiting its CPU usage to no more than 1.5 CPUs
docker run -d --name cpu_limited_container --cpus="1.5" nginx