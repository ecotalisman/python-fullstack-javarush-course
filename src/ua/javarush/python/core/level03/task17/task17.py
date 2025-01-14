# Odd Number Printer

# Write a program that prints numbers from 1 to 100, skipping even numbers.
# Use a while loop and the continue statement to skip even numbers.

### 🇺🇦 Ukrainian version:
# Непарний

# Напишіть програму, яка виводить числа від 1 до 100, пропускаючи парні числа.
# Використовуйте цикл while та оператор continue для пропуску парних чисел.

# Write your code here
i = 1
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
