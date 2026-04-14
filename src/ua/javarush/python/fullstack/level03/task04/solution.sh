# Removing a Docker Image
# Remove the my_python_app image that was created earlier.
# The image must no longer appear in the list of local images.
#
# Requirements:
# • The Docker `rmi` command must be used to remove the image named `my_python_app`.
# • After running the removal command, the local image list obtained with the `docker images` command
#   must not contain the image named `my_python_app`.
# • The removal command must execute without errors and confirm the successful deletion of the `my_python_app` image.
#
# ## 🇺🇦 Ukrainian version:
#
# Видалення Docker Image
# Видаліть образ my_python_app, який був створений раніше.
# Образ більше не повинен відображатися у списку локальних образів.
#
# Вимоги:
# • Необхідно використовувати команду Docker `rmi` для видалення образу з ім'ям `my_python_app`.
# • Після виконання команди видалення, локальний список образів, отриманий за допомогою команди `docker images`,
#   не повинен містити образ з ім'ям `my_python_app`.
# • Команда видалення повинна виконуватись без помилок і підтверджувати успішне видалення образу `my_python_app`.

# Remove the my_python_app image that was created earlier.
docker rmi my_python_app

# Check that the image no longer appears in the list of local images
docker images