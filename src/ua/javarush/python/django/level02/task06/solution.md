# Configuring VSCode for Working with Django
#
# 1. Install Visual Studio Code and the required extensions for Python and Django.
#
# 2. Select the Python interpreter from your virtual environment.
#
# 3. Configure the built-in terminal and the `launch.json` file for debugging Django applications.
#
# Requirements:
#
# 1. Download and install Visual Studio Code on your computer.
# 2. Install extensions for working with Python and Django, such as "Python" and "Django" in VSCode.
# 3. The Python interpreter must be configured in VSCode by selecting it from the project’s virtual environment.
# 4. Configure the built-in terminal in VSCode so that it uses the project’s virtual environment.
# 5. The `launch.json` file must be configured for debugging Django applications, including specifying the server startup command and the required configurations.
# 6. After completing all steps, the configuration must be checked by running the Django application in debug mode through VSCode.
#
# 🇺🇦 Ukrainian version:
#
# Налаштування VSCode для роботи з Django
#
# 1. Встановіть Visual Studio Code та необхідні розширення для Python і Django.
#
# 2. Оберіть Python-інтерпретатор із вашого віртуального оточення.
#
# 3. Налаштуйте вбудований термінал та файл `launch.json` для відлагодження Django-додатків.
#
# Вимоги:
#
# 1. Завантажте та встановіть Visual Studio Code на ваш комп'ютер.
# 2. Встановіть розширення для роботи з Python та Django, такі як "Python" та "Django" у VSCode.
# 3. Потрібно налаштувати Python-інтерпретатор у VSCode, обираючи його з віртуального оточення проєкту.
# 4. Налаштуйте вбудований термінал у VSCode так, щоби він використовував віртуальне оточення проєкту.
# 5. Файл `launch.json` має бути налаштований для відлагодження Django-додатків, включаючи вказання команди запуску сервера та необхідних конфігурацій.
# 6. Після виконання всіх кроків необхідно перевірити працездатність налаштувань, запустивши Django-додаток у відлагоджувальному режимі через VSCode.

## Step 1. Installing VSCode and the Required Extensions

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).

2. Install extensions for working with Python and Django:
   - **Python** (Microsoft)
   - **Django** (Batisteo or another suitable extension)

## Step 2. Creating and Configuring a Virtual Environment

1. In the project root, create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **On Unix/MacOS:**
     ```bash
     source venv/bin/activate
     ```

3. Install Django version 5.1:
   ```bash
   pip install django==5.1
   ```

## Step 3. Configuring VSCode

1. Open your project in VSCode.

2. Select the Python interpreter from the created virtual environment:
   - Open the Command Palette (Ctrl+Shift+P) and select the **Python: Select Interpreter** command.
   - Choose the interpreter located in the `venv` folder, for example `venv/bin/python` or `venv\Scripts\python.exe` for Windows.

3. The **.vscode/settings.json** file, see above, will configure the interpreter and ensure automatic activation of the virtual environment in the VSCode terminal.

## Step 4. Configuring Django Debugging

1. The **.vscode/launch.json** file contains the configuration for debugging Django applications:
   - When the debugger is started with F5, the following command will be executed:
     ```bash
     python manage.py runserver --noreload
     ```
   - Using the `--noreload` parameter ensures that breakpoints will not be reset during automatic server restart.

2. Start debugging by pressing F5 and make sure that the Django server starts in debug mode through the built-in VSCode terminal.

## Configuration Check

- The **manage.py** file must be located in the project root.
- If everything is configured correctly, you will be able to set breakpoints directly in your Django application code and debug it through VSCode.
