# Calculating Factorial

# Write a function factorial(n) that takes an integer n and returns its factorial.
# If n is 0, the function should return 1.
# The factorial of n is denoted as n! and is the product of all numbers from 1 to n.

### 🇺🇦 Ukrainian version:

# Обчислення факторіалу

# Напишіть функцію factorial(n), яка приймає ціле число n і повертає його факторіал. Якщо n дорівнює 0, функція повинна повернути 1.
# Факторіал числа n позначається як n! і є добутком усіх чисел від 1 до n.

# Write your code here
def factorial(n):
    if n > 0:
        fact = 1
        for num in range(2, n + 1):
            fact *= num
        return fact
    else:
        return 1

print(factorial(4))