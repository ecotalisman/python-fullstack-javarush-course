# Infinity is Not the Limit

# Write a program that takes any number of numbers and prints their sum.
# The program should:
# Define a function sum_numbers(*args) that accepts any number of numbers.
# Calculate the sum of all passed numbers.
# Print the result.

### 🇺🇦 Ukrainian version:

# Нескінченність не межа.

# Напишіть програму, яка приймає довільну кількість чисел і виводить їхню суму.
# Програма повинна:
# Визначити функцію sum_numbers(*args), яка приймає довільну кількість чисел.
# Обчислити суму всіх переданих чисел.
# Вивести результат.

# Write your code here
def sum_numbers(*args):
    sums = 0
    for item in args:
        sums += item
    return sums

print(sum_numbers(1, 2, 3))
