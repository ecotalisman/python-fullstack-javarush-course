# Using traceback

# Write a function divide_numbers that takes two arguments and divides the first number by the second.
# If a ZeroDivisionError exception occurs, catch it and print the stack trace using the traceback module.

### 🇺🇦 Ukrainian version:

# Використання traceback

# Напишіть функцію divide_numbers, яка приймає два аргументи та ділить перше число на друге.
# Якщо виникає виключення ZeroDivisionError, перехопіть його і виведіть стек-трейс, використовуючи модуль traceback.

# Write your code here
import traceback

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("An exception occurred: ")
        traceback.print_exc()

divide_numbers(1, 0)
