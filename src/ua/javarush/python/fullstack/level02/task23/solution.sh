# Limiting Container Swap Memory Usage
# Run a container using the nginx image, limiting it to 512 MB of RAM and 512 MB of swap memory.
# Name the container swap_limited_container.
#
# Requirements:
# • The container must be started using the nginx image.
# • The container must be configured to use no more than 512 MB of RAM.
# • The container must be configured to use no more than 512 MB of swap memory.
# • The container must be assigned the name swap_limited_container.
#
# ## 🇺🇦 Ukrainian version:
#
# Обмеження обсягу підкачки пам'яті контейнера
# Запустіть контейнер із образом nginx, обмеживши використання 512 MB оперативної пам'яті та 512 MB підкачки (swap).
# Назвіть контейнер swap_limited_container.
#
# Вимоги:
# • Контейнер має бути запущений з використанням образу nginx.
# • Контейнер має бути налаштований таким чином, щоб використовувати не більше 512 MB оперативної пам'яті.
# • Контейнер має бути налаштований таким чином, щоб використовувати не більше 512 MB підкачки (swap).
# • Контейнеру має бути присвоєне ім'я swap_limited_container.

# Run a container using the nginx image, limiting it to 512 MB of RAM and 512 MB of swap memory
docker run -d --name swap_limited_container --memory=512m --memory-swap=1024m nginx