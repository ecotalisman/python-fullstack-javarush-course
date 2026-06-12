# Working with Migrations
#
# 1. Create a new Django project and name it `myproject`.
#
# 2. Add a new application named `myapp` to your project using the `startapp` command.
#
# 3. Check the migration status using the `showmigrations` command.
#
# 4. Run the `makemigrations` and `migrate` commands to prepare the project for working with the database.
#
# Requirements:
#
# 1. The program must create a new Django project named `myproject` using the `django-admin startproject myproject` command.
# 2. The program must create a new application `myapp` in the project using the `startapp` command.
# 3. The program must use the `python manage.py showmigrations` command to display information about the current migration status.
# 4. The program must use the `python manage.py makemigrations` command to create new migrations based on changes in the models.
# 5. The program must apply migrations using the `python manage.py migrate` command.
# 6. All commands must be executed using the `manage.py` file provided by Django.
#
# 🇺🇦 Ukrainian version:
#
# Робота з міграціями
#
# 1. Створи новий Django-проєкт, назви його `myproject`.
#
# 2. Додай у свій проєкт новий застосунок з іменем `myapp` за допомогою команди `startapp`.
#
# 3. Перевір стан міграцій за допомогою команди `showmigrations`.
#
# 4. Виконай команди `makemigrations` та `migrate`, щоб підготувати проєкт до роботи з базою даних.
#
# Вимоги:
#
# 1. Програма має створити новий Django-проєкт з іменем `myproject`, використовуючи команду `django-admin startproject myproject`.
# 2. Програма має створити новий застосунок `myapp` у проєкті, використовуючи команду `startapp`.
# 3. Програма має використати команду `python manage.py showmigrations` для виведення інформації про поточний стан міграцій.
# 4. Програма має використати команду `python manage.py makemigrations` для створення нових міграцій на основі змін у моделях.
# 5. Програма має застосувати міграції, використовуючи команду `python manage.py migrate`.
# 6. Усі команди мають бути виконані за допомогою файла `manage.py`, який надає Django.

# 1. Create a Django project named myproject
django-admin startproject myproject

# Go to the project directory
cd myproject

# 2. Create a new application named myapp
python manage.py startapp myapp

# 3. Check the migration status
python manage.py showmigrations

# 4. Generate migrations based on the default Django models
python manage.py makemigrations

# Apply the migrations to the database
python manage.py migrate
