# Complete Network Isolation
# Create a container based on the BusyBox image
# that has no network activity at all, using the none network driver.
# The container must not have any network interface.
#
# Requirements:
# • The container must be created based on the official BusyBox image.
# • When creating the container, the none network driver must be used for complete network isolation.
# • The container must not have any active network interfaces, ensuring the absence of any network activity.
#
# ## 🇺🇦 Ukrainian version:
#
# Повна ізоляція мережі
# Створіть контейнер на основі образу BusyBox,
# який не матиме жодної мережевої активності, використовуючи мережевий драйвер none.
# Контейнер не повинен мати мережевого інтерфейсу.
#
# Вимоги:
# • Контейнер має бути створений на основі офіційного образу BusyBox.
# • Під час створення контейнера необхідно використовувати мережевий драйвер none для повної ізоляції мережі.
# • Контейнер не повинен мати активних мережевих інтерфейсів, забезпечуючи відсутність будь-якої мережевої активності.

# Creating a container using the none network driver
docker run -d --network none --name my_container busybox sleep infinity