# Searching for PostgreSQL-Related Images
# Find images related to PostgreSQL through the command line using the docker search command.
# Visually determine how many stars the official PostgreSQL image has.
#
# Requirements:
# • The script must use the docker search command to search for images related to postgres through the command line.
# • The script must display a list of images that contain "postgres" in their name or description.
# • The script must visually provide information about the number of stars of the official postgres image.
#
# ## 🇺🇦 Ukrainian version:
#
# Знайдіть образи, пов’язані з PostgreSQL, через командний рядок, використовуючи команду docker search.
# Візуально визначте, скільки зірок має офіційний образ PostgreSQL.
#
# Вимоги:
# • Скрипт повинен використовувати команду docker search для виконання пошуку образів, пов'язаних із postgres,
# через командний рядок.
# • Скрипт має відобразити список образів, що містять "postgres" у їх назві або описі.
# • Скрипт повинен візуально надати інформацію про кількість зірок в офіційного образу postgres.

# Searching for images related to PostgreSQL
docker search postgres

# Determining the number of stars of the official postgres image
stars=$(docker search postgres --filter "is-official=true" --format "{{.StarCount}}")
echo "The official postgres image has $stars stars"