# Fibonacci Generator

# Write a program that creates a generator based on a function to generate Fibonacci numbers.
# The program should:
# Define a function fibonacci() that uses the yield keyword to generate Fibonacci numbers.
# Create a generator object and use it to output the first 10 Fibonacci numbers.

### 🇺🇦 Ukrainian version:

# Генератор Фібоначчі.

# Напишіть програму, яка створює генератор на основі функції для генерації чисел Фібоначчі.
# Програма повинна:
# Визначити функцію fibonacci(), яка використовує ключове слово yield для генерації чисел Фібоначчі.
# Створити об'єкт-генератор і використовувати його для виведення перших 10 чисел Фібоначчі.

# Write your code here
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))