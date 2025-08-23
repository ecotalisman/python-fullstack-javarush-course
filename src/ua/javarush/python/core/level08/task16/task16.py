# Platform

# Write a program that retrieves and displays information about the current operating system
# and platform using the platform library. The program should:
# - Retrieve and display the name of the operating system.
# - Retrieve and display the computer's network name (hostname).
# - Retrieve and display the version of the operating system.
# - Retrieve and display the processor architecture.
# - Retrieve and display the Python version.

### 🇺🇦 Ukrainian version:

# Платформа.

# Напишіть програму, яка отримує та виводить інформацію про поточну операційну систему
# та платформу за допомогою бібліотеки platform. Програма повинна:
# Отримати та вивести ім'я операційної системи.
# Отримати та вивести ім'я комп'ютера у мережі (hostname).
# Отримати та вивести версію операційної системи.
# Отримати та вивести архітектуру процесора.
# Отримати та вивести версію Python.

# Write your code here
import platform

print(platform.system())
print(platform.node())
print(platform.release())
print(platform.architecture())
print(platform.python_version())