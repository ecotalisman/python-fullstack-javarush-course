# Sorting Time Estimation

# Write a program that estimates how long it would take to sort 1 billion numbers
# using three algorithms with the following time complexities:
# 1) 100 * n * ln(n)
# 2) 10 * n^2
# 3) n^3
# Print these three values.

### 🇺🇦 Ukrainian version:

# Рахунок часу сортування

# Напиши програму, яка буде рахувати, скільки триватиме сортування 1 млрд чисел трьома алгоритмами.
# Складність першого алгоритму: 100 * n * ln(n).
# Складність другого алгоритму: 10 * n^2.
# Складність третього алгоритму: n^3.
# Виведіть три ці числа на екран.

# Write your code here
from math import log

n = 1_000_000_000

a = 100 * n * log(n)
b = 10 * (n ** 2)
c = n ** 3

print(a)
print(b)
print(c)
