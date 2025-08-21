# Repeat Decorator

# Write a program that creates a decorator to call a function multiple times.
# The program should:
# Define a decorator repeat(num_times) that takes the number of repetitions as an argument.
# Apply the decorator to the say_hello(name) function, which prints a greeting message.
# Call the say_hello(name) function.

### 🇺🇦 Ukrainian version:

# Багаторазовий декоратор.

# Напишіть програму, яка створює декоратор для повторного виклику функції задану кількість разів.
# Програма повинна:
# Визначити декоратор repeat(num_times), який приймає кількість повторів як аргумент.
# Застосувати декоратор до функції say_hello(name), яка виводить привітальне повідомлення.
# Викликати функцію say_hello(name).

# Write your code here
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return  decorator_repeat

@repeat(num_times=3)
def say_hello(name):
    print(f"Hello, {name}")

say_hello("World!")
