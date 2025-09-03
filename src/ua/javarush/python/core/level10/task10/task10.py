# Stack Trace Analysis

# Write a function complex_operation that calls several nested functions and may raise an exception.
# If an exception occurs, catch it and extract the raw stack trace information
# using traceback.extract_tb().
# Print information about each stack frame (file, line, function name, line text).

### 🇺🇦 Ukrainian version:

# Аналіз стек-трейс

# Напишіть функцію complex_operation, яка викликає декілька вкладених функцій і може викликати виключення.
# Якщо виникає виключення, перехопіть його і витягніть "сирі" відомості про
# трасування стека з використанням traceback.extract_tb().
# Виведіть інформацію про кожен фрейм стека (файл, рядок, ім'я функції, текст рядка).

# Write your code here
import sys
import traceback


def function_a():
    return 1 / 0

def function_b():
    function_a()

def complex_operation():
    try:
        function_b()
    except ZeroDivisionError:
        tb = sys.exc_info()[2]
        for frame in traceback.extract_tb(tb):
            print(f"File: {frame.filename}")
            print(f"Line: {frame.lineno}")
            print(f"Function: {frame.name}")
            print(f"Text: {frame.line}")
            print("-" * 40)

complex_operation()
