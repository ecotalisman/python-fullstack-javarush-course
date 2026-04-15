# Using Multiple RUN Commands
# Create a Dockerfile for an application based on Ubuntu, in which Git and curl are installed
# using a single RUN command. After installation, delete the package cache to reduce the image size.
#
# Requirements:
# • The Dockerfile must use Ubuntu as the base image.
# • The Dockerfile must contain a RUN command that installs the Git and curl packages.
# • The Dockerfile must include deletion of the package cache in the same RUN command to reduce the size of the final image.
# • Git and curl must be installed in a single RUN command followed by deletion of the package cache in the same command.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання кількох команд RUN
# Створіть Dockerfile для застосунку на основі Ubuntu, в якому встановіть Git і curl через одну команду RUN.
# Після встановлення видаліть кеш пакетів, щоб зменшити розмір образу.
#
# Вимоги:
# • Dockerfile повинен використовувати Ubuntu як базовий образ.
# • Dockerfile повинен містити команду RUN, яка встановлює пакети Git і curl.
# • Dockerfile повинен включати видалення кешу пакетів у тій самій команді RUN, щоб зменшити розмір кінцевого образу.
# • Git і curl повинні бути встановлені в одній команді RUN з подальшим видаленням кешу пакетів у тій самій команді.

# Using the Ubuntu image
FROM ubuntu

# Updating the package index, installing Git and curl, then deleting the package cache
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Setting the working directory
WORKDIR /app

# Default command
CMD ["bash"]