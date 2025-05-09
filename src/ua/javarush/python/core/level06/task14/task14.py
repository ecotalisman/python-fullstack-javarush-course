# Set Difference

# Write a program that creates two sets, each with 10 random numbers.
# The first set should contain random numbers from 1 to 20, and the second set should contain random numbers from 10 to 30.
# The program should find the difference of the first set from the second using the difference() method.
# It should also find the symmetric difference using the symmetric_difference() method.
# The program should display both results.

### 🇺🇦 Ukrainian version:

# Різниця множин

# Напишіть програму, яка створює дві множини, кожна з 10 випадкових чисел.
# Перша множина містить випадкові числа в діапазоні від 1 до 20, а друга множина містить випадкові числа в діапазоні від 10 до 30.
# Програма повинна знайти різницю першої множини з другою з використанням методу difference().
# І симетричну різницю з використанням методу symmetric_difference().
# Програма повинна вивести обидва результати.

# Write your code here
from random import randint as r
l1 = [(r(1, 20)) for i in range(10)]
l2 = [(r(10, 30)) for i in range(10)]

s1 = set(l1)
s2 = set(l2)

difference_set = s1.difference(s2)
symmetric_difference_set = s1.symmetric_difference(s2)

print(f"Difference set: {difference_set}")
print(f"Symmetric difference set: {symmetric_difference_set}")
