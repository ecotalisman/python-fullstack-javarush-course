# Creating a Custom Network
# Create a custom network in Docker to check network functionality.
# Make sure that the new network appears in the list of networks.
#
# Hint:
# 1. Create a network.
# 2. Display the list of networks.
#
# Requirements:
# • Create a new custom network in Docker using the appropriate command.
# • After creating the network, display a list of all available Docker networks to make sure the new network is present.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення користувацької мережі
# Створіть користувацьку мережу в Docker для перевірки мережевої функціональності.
# Переконайтеся, що нова мережа з'явилася в списку мереж.
#
# Підказка:
# 1. Створіть мережу.
# 2. Відобразіть список мереж.
#
# Вимоги:
# • Створіть нову користувацьку мережу в Docker, використовуючи відповідну команду.
# • Після створення мережі виведіть список усіх доступних мереж в Docker, щоб переконатися в наявності нової мережі.

# Creating a custom network
docker network create my_test_network

# Displaying the list of networks
docker network ls