# Raising a Standard Exception

# Write a function check_positive that takes a number and checks if it is positive.
# If the number is negative or zero, the function should raise a ValueError with the message "Number must be positive".

### 🇺🇦 Ukrainian version:

# Запуск стандартної виключної ситуації

# Напишіть функцію check_positive, яка приймає число і перевіряє, чи є воно додатним.
# Якщо число від'ємне або дорівнює нулю, функція повинна викликати виключення ValueError з повідомленням "Number must be positive".

# Write your code here
def check_positive(num):
    if num < 1:
        raise ValueError("Number must be positive")

try:
    check_positive(-1)
except ValueError as e:
    print(e)
