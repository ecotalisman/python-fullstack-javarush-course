# Running a Container on the host Network
# Create a container with Nginx using the host network driver.
# The container must use the network stack of the host machine directly.
#
# Requirements:
# • The container must be started with the host network driver, which allows it to use the host machine's network stack directly.
# • The created container must contain an installed and configured Nginx web server.
# • The container configuration must ensure the use of the host machine's IP address and port without changing network settings.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск контейнера в host-мережі
# Створіть контейнер із Nginx, використовуючи мережевий драйвер host.
# Контейнер має використовувати мережевий стек хостової машини напряму.
#
# Вимоги:
# • Контейнер має бути запущений із мережевим драйвером host, що дозволяє йому використовувати мережевий стек хостової машини напряму.
# • Створюваний контейнер має містити встановлений і налаштований вебсервер Nginx.
# • Конфігурація контейнера має забезпечувати використання IP-адреси та порту хостової машини без зміни мережевих налаштувань.

# Starting a Docker container with Nginx using the host network mode
docker run -d --network host --name my_nginx nginx