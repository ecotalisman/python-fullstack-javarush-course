# Using the RUN Instruction
# Create a Dockerfile for an image based on ubuntu:20.04.
# In the Dockerfile, install curl and git, and then clear the cache
# to reduce the image size.
#
# Requirements:
# • The Dockerfile must start by specifying the ubuntu:20.04 base image.
# • The Dockerfile must contain a RUN instruction that installs the curl and git packages using the apt package manager.
# • The Dockerfile must include a command to clear the apt cache after installing curl and git to reduce the size of
# the final image.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання інструкції RUN
# Створіть Dockerfile для образу на основі ubuntu:20.04.
# У Dockerfile виконайте установку curl і git, а потім очистьте кеш для зменшення розміру образу.
#
# Вимоги:
# • Dockerfile має починатися з вказівки базового образу ubuntu:20.04.
# • Dockerfile має містити інструкцію RUN, яка встановлює пакети curl і git через пакетний менеджер apt.
# • Dockerfile має включати команду для очищення кешу apt після установки curl і git, щоб зменшити розмір фінального образу.

# Using the Ubuntu 20.04 base image
FROM ubuntu:20.04

# Installing curl and git with cache cleanup
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*
