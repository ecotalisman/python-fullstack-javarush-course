# Data Conversion

# Write a function convert_and_sum that takes two arguments as strings,
# converts them into integers, and returns their sum.
# Handle exceptions that may occur during the conversion of strings into numbers
# (for example, if invalid values are passed).

### 🇺🇦 Ukrainian version:

# Перетворення даних.

# Напишіть функцію convert_and_sum, яка приймає два аргументи у вигляді рядків,
# перетворює їх у цілі числа і повертає їхню суму.
# Опрацюйте виключення, які можуть виникнути під час перетворення рядків у числа
# (наприклад, якщо передано некоректні значення).

# Write your code here
def convert_and_sum(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return "Invalid input, please enter a number"

num_1 = input("Enter a number one: ")
num_2 = input("Enter a number two: ")
print(convert_and_sum(num_1, num_2))
