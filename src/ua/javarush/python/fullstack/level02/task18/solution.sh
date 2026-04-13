# Running a Command Without Attaching to the Terminal
# Inside the container named db_container, create a new file named backup.sql
# in the /data directory. Run this command in detached mode, without attaching to the terminal.
#
# Requirements:
# • The container must be created with the name db_container to match the task requirements.
# • A file named backup.sql must be created in the /data directory inside the db_container container.
# • The command that creates the backup.sql file must be executed in detached mode, without attaching to the terminal.
#
# ## 🇺🇦 Ukrainian version:
#
# Виконання команди без прив’язки до терміналу
# У контейнері з ім’ям db_container створіть новий файл backup.sql у директорії /data.
# Виконайте цю команду в режимі без прив’язки до терміналу.
#
# Вимоги:
# • Контейнер має бути створений з ім’ям db_container, щоб відповідати умовам задачі.
# • Необхідно створити файл з ім’ям backup.sql у директорії /data всередині контейнера db_container.
# • Команда зі створення файлу backup.sql має виконуватись у режимі detach, тобто без прив’язки до терміналу.

# Create a new file named backup.sql in the /data directory inside the db_container container
docker exec -d db_container touch /data/backup.sql