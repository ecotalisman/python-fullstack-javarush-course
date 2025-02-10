# Sorting Without Sorting

# Write a program that creates a list of 10 random numbers in the range from 1 to 100.
# Then, the program should create a copy of this list and sort the copy in ascending order without modifying the original list.
# The program should display both the original and sorted lists.

### 🇺🇦 Ukrainian version:

# Сортування без сортування

# Напишіть програму, яка створює список із 10 випадкових чисел у діапазоні від 1 до 100.
# Потім програма повинна створити копію цього списку і відсортувати копію за зростанням, не змінюючи вихідний список.
# Програма повинна вивести вихідний та відсортований списки.

# Write your code here
from random import randint

l = [randint(1, 100) for _ in range(10)]
n = list(sorted(l))
print(l, "\n", n, sep="")