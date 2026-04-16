# Combining Commands to Reduce Layers
# Optimize the Dockerfile to reduce the number of layers. Instead of multiple RUN instructions,
# combine them into a single command, minimizing the number of layers and temporary files.
# Use the ubuntu base image and install curl and git.
#
# Requirements:
# • The Dockerfile must use the ubuntu base image to create the container.
# • The RUN instructions must be combined into a single command to minimize the number of layers in the Dockerfile.
# • The Dockerfile must contain commands to install curl and git in a container based on the ubuntu image.
#
# ## 🇺🇦 Ukrainian version:
#
# Об'єднання команд для зменшення шарів
# Оптимізуйте Dockerfile, щоб зменшити кількість шарів. Замість кількох інструкцій RUN,
# об'єднайте їх в одну команду, мінімізуючи кількість шарів і тимчасових файлів.
# Використовуйте базовий образ ubuntu та встановіть curl і git.
#
# Вимоги:
# • Dockerfile має використовувати базовий образ ubuntu для створення контейнера.
# • Інструкції RUN мають бути об'єднані в одну команду, щоб мінімізувати кількість шарів у Dockerfile.
# • Dockerfile має містити команди для встановлення curl і git у контейнер на основі образу ubuntu.

# Using the Ubuntu base image
FROM ubuntu:latest

# Updating the package list in the package manager
# Installing curl, git and cleaning the apt package manager cache
# Removing cached package lists to reduce the image size
RUN apt-get update && apt-get install -y curl && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*