# Maximalist
import random


# Write a function find_max(a, b) that takes two numbers as arguments and returns the larger of the two.
# If the numbers are equal, the function should return either of them.
# Then write a program that asks the user for two numbers, calls this function, and prints the result.

### 🇺🇦 Ukrainian version:

# Максималіст

# Напишіть функцію find_max(a, b), яка приймає два числа як аргументи і повертає більше з них.
# Якщо числа рівні, функція повинна повернути будь-яке з них.
# Потім напишіть програму, яка запитує у користувача два числа, викликає цю функцію і виводить результат.

# Write your code here
def find_max(a, b):
    if a >= b:
        return a
    else:
        return b

one = int(input("Enter number one: "))
two = int(input("Enter number two: "))

print(find_max(one, two))