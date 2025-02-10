# Clearing the List

# Write a program that creates a list of 10 random numbers in the range from 1 to 20.
# Then, the program should remove all even numbers from the list using a loop.
# The program should display both the original and updated lists.

### 🇺🇦 Ukrainian version:

# Очищуємо список

# Напишіть програму, яка створює список з 10 випадкових чисел у діапазоні від 1 до 20.
# Потім програма повинна видалити зі списку всі парні числа з використанням циклу.
# Програма повинна вивести початковий та оновлений списки.

# Write your code here
from random import randint

l = [randint(1, 20) for _ in range(10)]
print(l)
for n in l.copy():
    if n % 2 == 0:
        l.remove(n)
print(l)