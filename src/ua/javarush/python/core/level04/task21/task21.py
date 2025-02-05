# Summing All Numbers

# Write a function sum_numbers(*args: int) -> int that takes any number of integer arguments and returns their sum.
# Then write a program that calls this function with different sets of arguments and prints the result.

### 🇺🇦 Ukrainian version:

# Сумуємо всі числа

# Напишіть функцію sum_numbers(*args: int) -> int, яка приймає довільну кількість цілих чисел як аргументи і повертає їхню суму.
# Потім напишіть програму, яка викликає цю функцію з різними наборами аргументів і виводить результат.

# Write your code here
def sum_numbers(*args: int) -> int:
    sums = 0
    for item in args:
        sums += item
    return sums

print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2))
print(sum_numbers(1, 2, 3, 4))