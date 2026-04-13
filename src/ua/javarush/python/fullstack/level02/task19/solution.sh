# Installing Packages Inside a Container
# Install the Vim text editor inside the container named my_container.
# Before installation, update the package list using the docker exec command.
#
# Requirements:
# • The Vim text editor must be installed inside the container named my_container.
# • Before installing Vim, the package list inside the my_container container must be updated.
# • The docker exec command must be used to update the package list and install Vim.
#
# ## 🇺🇦 Ukrainian version:
#
# Встановлення пакетів всередині контейнера
# У контейнері з ім'ям my_container виконайте встановлення текстового редактора Vim.
# Перед встановленням оновіть список пакетів, використовуючи команду docker exec.
#
# Вимоги:
# • У контейнері з ім'ям my_container має бути встановлений текстовий редактор Vim.
# • Перед встановленням Vim необхідно оновити список пакетів всередині контейнера my_container.
# • Для виконання оновлення списку пакетів і встановлення Vim необхідно використовувати команду docker exec.

# Updating the package list inside the my_container container
docker exec my_container apt-get update

# Installing the Vim text editor inside the my_container container
docker exec my_container apt-get install -y vim