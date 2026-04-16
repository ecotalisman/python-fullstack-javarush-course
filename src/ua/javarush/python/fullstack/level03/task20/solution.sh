# Filtering Images by Tag
# Write a command that filters and displays only images from the ubuntu repository
# with the 20.04 tag. The output must display only the correct information about the selected image.
#
# Requirements:
# • The command must use the `docker images` utility to display the list of available Docker images.
# • The command must include filtering by repository to display only images from the `ubuntu` repository.
# • The command must include filtering by tag to display only images with the `20.04` tag.
# • The output of the command must include information exclusively about the selected images
#   that match the `ubuntu` repository and the `20.04` tag.
#
# ## 🇺🇦 Ukrainian version:
#
# Фільтрація образів за тегом
# Напишіть команду, яка відфільтрує та відобразить лише образи з репозиторію ubuntu з тегом 20.04.
# Вивід повинен відображати тільки правильну інформацію про обраний образ.
#
# Вимоги:
# • Команда повинна використовувати утиліту `docker images` для відображення списку доступних Docker-образів.
# • Команда повинна включати фільтрацію за репозиторієм, щоб відобразити лише образи з репозиторію `ubuntu`.
# • Команда повинна включати фільтрацію за тегом, щоб відобразити лише образи з тегом `20.04`.
# • Вивід команди повинен включати інформацію виключно про обрані образи, які відповідають репозиторію `ubuntu` та тегу `20.04`.

# Command to filter and display only images from the ubuntu repository with the 20.04 tag
docker images ubuntu:20.04