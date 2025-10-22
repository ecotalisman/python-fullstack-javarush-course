# Runtime Estimation

# Write a program that estimates how long it would take to find a solution
# for n = 100 using three algorithms with the following time complexities:
# 1) 100 * n^10
# 2) 10 * 2^n
# 3) n!
# Print these three values.

### 🇺🇦 Ukrainian version:

# Підрахунок часу роботи

# Напиши програму, яка буде рахувати, скільки триватиме пошук рішення для 100 даних трьома алгоритмами.
# Складність першого алгоритму 100*n^10.
# Складність другого алгоритму 10*2^n.
# Складність третього алгоритму n!.
# Виведіть три цих числа на екран.

# Write your code here
import math

n = 100
a = 100 * n ** 10
b = 10 * 2 ** n
c = math.factorial(n)

print(a)
print(b)
print(c)
