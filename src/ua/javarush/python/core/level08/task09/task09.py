# Decorator

# Write a program that creates a simple decorator for logging function calls.
# The program should:
# Define a decorator log_decorator that prints a message before and after the function call.
# Apply the decorator to the greet() function, which prints a greeting message.
# Call the greet() function.

### 🇺🇦 Ukrainian version:

# Декоратор.

# Напишіть програму, яка створює простий декоратор для логування викликів функції.
# Програма повинна:
# Визначити декоратор log_decorator, який виводить повідомлення перед та після виклику функції.
# Застосувати декоратор до функції greet(), яка виводить привітальне повідомлення.
# Викликати функцію greet().

# Write your code here
def log_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

@log_decorator
def greet():
    print("Hello!")

greet()