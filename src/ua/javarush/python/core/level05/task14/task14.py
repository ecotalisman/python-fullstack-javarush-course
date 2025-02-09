# Filtering

# Write a program that creates a list of 20 random numbers in the range from 1 to 100 using List Comprehension.
# Then, using List Comprehension, create a new list that contains only even numbers from the original list.
# The program should display both lists.

### 🇺🇦 Ukrainian version:

# Фільтрація

# Напиши програму, яка створює список з 20 випадкових чисел у діапазоні від 1 до 100 з використанням List Comprehension.
# Потім з використанням List Comprehension створює новий список, що містить лише парні числа з початкового списку.
# Програма повинна вивести обидва списки.

# Write your code here
from random import randint

l = [randint(1, 100) for x in range(20)]
n = [x for x in l if x % 2 == 0]
print(l)
print(n)