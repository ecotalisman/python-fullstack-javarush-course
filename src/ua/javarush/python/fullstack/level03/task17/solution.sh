# Viewing All Local Images
# Write a command to view all locally stored Docker images on your system.
# Format the output so that it contains only the repository name and the image tag.
#
# Requirements:
# • A Docker command must be used to display all locally stored images on the system.
# • The command output must be formatted to display only the repository name and the tag of each Docker image.
# • The output must not contain additional information such as the image ID, size, or creation date.
#
# ## 🇺🇦 Ukrainian version:
#
# Перегляд усіх локальних образів
# Напишіть команду для перегляду всіх локально збережених Docker-образів на вашій системі.
# Відформатуйте вивід так, щоб він містив тільки ім'я репозиторію та тег образу.
#
# Вимоги:
# • Необхідно використовувати Docker-команду, яка відображає всі локально збережені образи на системі.
# • Вивід команди має бути відформатований так, щоб відображалися тільки ім'я репозиторію та тег кожного Docker-образу.
# • Вивід не повинен містити додаткової інформації, такої як ідентифікатор образу, розмір і дата створення.

# Command to display locally stored Docker images with formatted output
docker images --format "{{.Repository}}:{{.Tag}}"