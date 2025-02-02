# Random Argument
import random


# Write a function print_random(a, b, c) that prints a randomly selected argument from the ones provided.

### 🇺🇦 Ukrainian version:

# Випадковий аргумент

# Напишіть функцію print_random(a,b,c), яка виводить на екран випадково вибраний переданий аргумент.

# Write your code here
def print_random(a, b, c):
    print(random.choice([a, b, c]))
print_random(1, 2, 3)