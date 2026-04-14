# Limiting CPU and Memory Usage for a Container
# Run a container based on the my_app image, limiting its usage to 2 CPUs and 1 GB of memory.
# Name the container resource_limited_container.
#
# Requirements:
# • The container must be started based on the my_app image.
# • The container must be limited to using 2 CPUs.
# • The container must be limited to using 1 GB of memory.
# • The container must be named resource_limited_container.
#
# ## 🇺🇦 Ukrainian version:
#
# Обмеження використання CPU та пам'яті контейнера
# Запустіть контейнер на основі образу my_app, обмеживши його використання 2 CPU та 1 GB пам'яті.
# Назвіть контейнер resource_limited_container.
#
# Вимоги:
# • Контейнер має бути запущений на основі образу my_app.
# • Контейнер повинен бути обмежений використанням 2 CPU.
# • Контейнер має бути обмежений використанням 1 GB пам'яті.
# • Контейнер має бути названий resource_limited_container.

# Run a container based on the my_app image, limiting its usage to 2 CPUs and 1 GB of memory
docker run -d --name resource_limited_container --cpus="2" --memory=1g my_app