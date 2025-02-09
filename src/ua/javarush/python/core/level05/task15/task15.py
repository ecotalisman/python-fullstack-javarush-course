# Sorting

# Write a program that creates a list of 10 random numbers in the range from 1 to 100.
# Then, sort the list in ascending and descending order.
# The program should display the original list, the list sorted in ascending order, and the list sorted in descending order.

### 🇺🇦 Ukrainian version:

# Сортування

# Напишіть програму, яка створює список із 10 випадкових чисел у діапазоні від 1 до 100.
# Потім сортує його за зростанням та спаданням.
# Програма повинна вивести початковий список, відсортований за зростанням та спаданням списки.

# Write your code here
from random import randint

l = [randint(1, 100) for n in range(10)]
print(l, "\n", sorted(l), "\n", sorted(l, reverse=True), sep="")