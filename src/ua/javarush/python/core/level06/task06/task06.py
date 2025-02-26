# Square Generator

# Write a program that creates a set of squares of numbers from 1 to 10 using a set comprehension.
# The program should display the generated set.

### 🇺🇦 Ukrainian version:

# Генератор квадратів

# Напишіть програму, яка створює множину квадратів чисел від 1 до 10 з використанням генератора множин.
# Програма повинна вивести отриману множину.

# Write your code here
s = {x ** 2 for x in range(1, 11)}
print(s)