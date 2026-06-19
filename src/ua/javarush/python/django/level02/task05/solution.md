# Installing and Configuring PyCharm
#
# 1. Install PyCharm from JetBrains.
#
# 2. Create a new Django project in PyCharm using the built-in template.
#
# 3. Configure a virtual environment.
#
# 4. Select the correct Python interpreter.
#
# Requirements:
#
# 1. Install the latest version of PyCharm from JetBrains to complete the task.
# 2. Create a new project in PyCharm using the built-in Django template tool.
# 3. Configure a virtual environment to isolate dependencies.
# 4. Select the correct Python interpreter that matches the Python version installed on the computer.
# 5. After configuring the project, PyCharm must correctly recognize Django and its dependencies so that the project can be run successfully.
#
# 🇺🇦 Ukrainian version:
#
# Встановлення та налаштування PyCharm
#
# 1. Встановіть PyCharm від JetBrains.
#
# 2. Створіть новий проект Django у PyCharm, використовуючи вбудований шаблон.
#
# 3. Налаштуйте віртуальне оточення.
#
# 4. Оберіть правильний інтерпретатор Python.
#
# Вимоги:
#
# 1. Встановіть останню версію PyCharm від JetBrains для виконання завдання.
# 2. Створіть новий проект у PyCharm, використовуючи вбудований інструмент для шаблонів Django.
# 3. Налаштуйте віртуальне оточення для ізоляції залежностей.
# 4. Оберіть правильний інтерпретатор Python, що відповідає встановленій на комп'ютері версії Python.
# 5. Після налаштування проекту PyCharm повинен коректно розпізнавати Django та його залежності, щоб проект міг успішно запускатися.

## Project Setup Steps

1. **Installing PyCharm:**  
   Make sure that you have the latest version of PyCharm from JetBrains installed.

2. **Opening the Project:**  
   Open this project in PyCharm. PyCharm will automatically recognize the structure of the Django project.

3. **Configuring the Virtual Environment:**  
   When opening the project, PyCharm will suggest creating a virtual environment. If this does not happen, follow these steps:
   - Go to *File* → *Settings* → *Project: myproject* → *Python Interpreter*.
   - Click the gear icon and select *Add Interpreter*.
   - Select *Virtualenv Environment* and confirm its creation.

4. **Selecting the Python Interpreter:**  
   Make sure that Python version 3.12 is selected as the interpreter for the virtual environment.

5. **Installing Dependencies:**  
   Open the terminal in PyCharm and run the command:
     pip install -r requirements.txt  
   This will install Django 5.1.

6. **Initial Migrations and Starting the Server:**  
   In the terminal, run:
     python manage.py migrate  
   Then start the server:
     python manage.py runserver  
   The server should start successfully, and Django should be correctly recognized.
