# Creating a Simple Django Model
#
# 1. Create an `Author` model that will contain the following fields:
#
# - `name`, a string field with a length of up to 100 characters.
#
# - `birth_date`, the date of birth.
#
# 2. Create and apply migrations.
#
# Requirements:
#
# 1. A model named `Author` must be created in the Django project.
# 2. The `Author` model must contain a string field `name`, limited to a length of up to 100 characters (`CharField`).
# 3. The `Author` model must contain a `birth_date` field for storing the date of birth (`DateField`).
# 4. All required attributes must be correctly specified for each field, such as `max_length` for `name`.
# 5. The process of creating and applying migrations must be completed to update the database by adding the new model.
# 6. Standard Django functions and classes must be used to implement the model and migrations, for example, `models.CharField`, `models.DateField`, `makemigrations`, and `migrate`.
#
# 🇺🇦 Ukrainian version:
#
# Створення простої моделі Django
#
# 1. Створи модель `Author`, яка міститиме такі поля:
#
# - `name` (рядкове поле, довжина до 100 символів).
#
# - `birth_date` (дата народження).
#
# 2. Створи і застосуй міграції.
#
# Вимоги:
#
# 1. У Django-проєкті повинна бути створена модель з іменем `Author`.
# 2. Модель `Author` повинна містити рядкове поле `name`, обмежене довжиною до 100 символів (CharField).
# 3. Модель `Author` повинна містити поле `birth_date` для збереження дати народження (DateField).
# 4. Для кожного поля мають бути правильно вказані всі необхідні атрибути, такі як `max_length` для `name`.
# 5. Повинен бути виконаний процес створення і застосування міграцій для оновлення бази даних із додаванням нової моделі.
# 6. Для реалізації моделі та міграцій мають бути використані стандартні функції та класи Django, наприклад `models.CharField`, `models.DateField`, `makemigrations`, `migrate`.

# Create and apply migrations
python manage.py makemigrations app
python manage.py migrate