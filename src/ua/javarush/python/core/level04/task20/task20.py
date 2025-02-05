# Using a nonlocal Variable

# Write a program that contains a nested function.
# The outer function outer_function() should declare a variable x and assign it the value 10.
# The inner function inner_function() should increase the value of x by 5 using the nonlocal statement.
# Then call the inner function and print the value of x in the outer function.

### 🇺🇦 Ukrainian version:

# Використання nonlocal змінної

# Напишіть програму, в якій є вкладена функція.
# Зовнішня функція outer_function() має оголошувати змінну x і присвоювати їй значення 10.
# Внутрішня функція inner_function() повинна збільшувати значення змінної x на 5, використовуючи оператор nonlocal.
# Потім викличте внутрішню функцію і виведіть значення змінної x у зовнішній функції.

# Write your code here
def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x += 5
        return x

    return print(inner_function())

outer_function()