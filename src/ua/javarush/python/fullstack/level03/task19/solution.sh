# Removing All Untagged Images
# Use a Docker command to remove all "dangling" images — images without tags
# that may remain after updates or failed builds. They must be removed successfully.
#
# Requirements:
# • A Docker command must be used to remove "dangling" images.
# • Searching for "dangling" images: Before removal, a search for all untagged images must be performed.
# • Removing all "dangling" images: All found "dangling" images must be successfully removed from the system.
#
# ## 🇺🇦 Ukrainian version:
#
# Видалення всіх образів без тегів
# Використовуйте команду Docker для видалення всіх "dangling" образів — образів без тегів,
# які можуть залишатися після оновлень чи невдалих збірок. Вони повинні бути успішно видалені.
#
# Вимоги:
# • Необхідно використовувати команду Docker для видалення "dangling" образів.
# • Пошук "dangling" образів: Перед видаленням повинен бути виконаний пошук усіх образів без тегів.
# • Видалення всіх "dangling" образів: Усі знайдені "dangling" образи повинні бути успішно видалені з системи.

# Removing all "dangling" images
docker rmi $(docker images -f "dangling=true" -q)