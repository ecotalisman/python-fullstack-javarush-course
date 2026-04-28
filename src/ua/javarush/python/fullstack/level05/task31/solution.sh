# Studying the Network Configuration
# You need to make sure that the webnet network,
# to which the web and db containers are connected,
# is configured correctly. Use the docker network inspect command
# to display information about the network and its connected containers.
#
# Requirements:
# • It is necessary to make sure that the network named webnet exists
#   and is available for use by containers.
# • The containers named web and db must be connected to the webnet network.
# • The docker network inspect command must be used to get detailed information
#   about the webnet network and the containers connected to it.
# • It is necessary to verify that the network configuration,
#   such as the driver and other parameters, matches the specified settings.
# • The web and db containers must be visible in the output
#   of the docker network inspect command as connected to the webnet network.
#
# ## 🇺🇦 Ukrainian version:
#
# Вивчення конфігурації мережі
# Вам необхідно переконатися, що мережа webnet,
# до якої підключені контейнери web та db, правильно налаштована.
# Використовуйте команду docker network inspect,
# щоб вивести інформацію про мережу та її підключені контейнери.
#
# Вимоги:
# • Необхідно переконатися, що мережа з ім'ям webnet існує та доступна для використання контейнерами.
# • Контейнери з назвами web та db повинні бути підключені до мережі webnet.
# • Потрібно використовувати команду docker network inspect для отримання детальної інформації про мережу webnet та підключені до неї контейнери.
# • Необхідно перевірити, що конфігурація мережі, така як драйвер, та інші параметри, відповідають заданим.
# • Контейнери web та db повинні бути видимі в виводі команди docker network inspect як підключені до мережі webnet.

# Make sure that the webnet network is created and active
docker network ls

# Use the docker network inspect command to display information about the webnet network
docker network inspect webnet

# Displaying information about the containers connected to the webnet network
docker network inspect webnet | grep -A 5 Containers

# Checking network attributes such as the driver and other parameters
docker network inspect webnet | grep -E '"Driver":|"Scope":|"EnableIPv6":|"Subnet":|"Gateway":'
