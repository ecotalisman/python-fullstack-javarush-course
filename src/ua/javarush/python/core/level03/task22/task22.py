# Pythagorean Table

# Write a program that asks the user for a number N and prints an NxN Pythagorean multiplication table using nested loops.
# The program should display only the numbers in the table.
# Example:
# 1   2   3   ...
# 2   4   6   ...
# 3   6   9   ...
# ...

### 🇺🇦 Ukrainian version:
# Таблиця Піфагора

# Напишіть програму, яка запитує у користувача число N і виводить таблицю множення Піфагора розміром NxN, використовуючи вкладені цикли.
# Програма повинна виводити лише числа таблиці.
# Приклад:
# 1   2   3   ...
# 2   4   6   ...
# 3   6   9   ...
# ...

# Write your code here
n = int(input("add number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end='\t')
    print()