# Clear but Random

# Write a program that creates a set of 10 random numbers in the range from 1 to 100.
# The program should extract a subset of all even numbers from this set and display it.

### 🇺🇦 Ukrainian version:

# Чіткий але випадковий

# Напишіть програму, яка створює множину з 10 випадкових чисел в діапазоні від 1 до 100.
# Програма повинна отримати підмножину всіх парних чисел з цієї множини і вивести його.

# Write your code here
from random import randint
s = {randint(1, 100) for _ in range(10)}
even_s = set(filter(lambda x: x % 2 == 0, s))
print(even_s)