# Multiple Decorators

# Write a program that uses multiple decorators for one function.
# The program should:
# Define two decorators decorator1 and decorator2 that log their calls.
# Apply both decorators to the say_hello function.
# Call the say_hello function.

### 🇺🇦 Ukrainian version:

# Множина декораторів.

# Напишіть програму, яка використовує кілька декораторів для однієї функції.
# Програма повинна:
# Визначити два декоратори decorator1 і decorator2, які логують свої виклики.
# Застосувати обидва декоратори до функції say_hello.
# Викликати функцію say_hello.

# Write your code here
def decorator1(func):
    def wrapper():
        print("Decorator-1")
        func()

    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator-2")
        func()

    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()