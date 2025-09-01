# Exception Handling

# Write a function safe_division that takes two numbers and performs their division.
# Handle exceptions that may occur when dividing by zero
# and when passing invalid values (e.g., a string instead of numbers).
# The function should return an error message or the result of the division.

### 🇺🇦 Ukrainian version:

# Обробка винятків.

# Напишіть функцію safe_division, яка приймає два числа і виконує їх ділення.
# Обробіть винятки, які можуть виникнути при діленні на нуль
# і при передачі некоректних значень (наприклад, рядка замість чисел).
# Функція повинна повертати повідомлення про помилку або результат ділення.

# Write your code here
def safe_division(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except (TypeError, ValueError):
        return "Invalid input, please enter a number"

num1 = input("Enter a number one: ")
num2 = input("Enter a number two: ")
print(safe_division(num1, num2))
