# Indexing

# Write a program that creates a set of random numbers in the range from 1 to 50.
# Then, the program should print all elements of the set along with their "indexes" using the enumerate() function.

### 🇺🇦 Ukrainian version:

# Індексація

# Напишіть програму, яка створює множину з випадкових чисел у діапазоні від 1 до 50.
# Потім програма має вивести всі елементи множини разом з їх "індексами", використовуючи функцію enumerate().

# Write your code here
from random import randint
import random

s = set(random.sample(range(1, 50), 10))
for index, el in enumerate(s, start=1):
    print(f"Index: {index}, Element: {el}")
