# Random Sets

# Write a program that generates:
# - One list of random elements from 0 to 99.
# - A second list of random elements from 50 to 125.
# Then, convert the lists into sets.
# Add the first set to the second set.
# Print the number of elements in the resulting set.

### 🇺🇦 Ukrainian version:

# Випадкові множини

# Напишіть програму, яка згенерує:
# Один список випадкових елементів від 0 до 99.
# Другий список випадкових елементів від 50 до 125.
# Потім перетворіть списки на множини.
# Додайте першу множину до другої.
# Виведіть кількість елементів отриманої множини на екран.

# Write your code here
from random import randint

lstOne = [randint(0, 99) for _ in range(20)]
lstTwo = [randint(50, 125) for _ in range(30)]

s1 = set(lstOne)
s2 = set(lstTwo)
s1.update(s2)
print(len(s1))
