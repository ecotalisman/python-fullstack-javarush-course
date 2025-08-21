# Execution Time

# Write a program that creates a decorator to measure the execution time of a function.
# The program should:
# Define a decorator time_decorator that measures and prints the execution time of a function.
# Apply the decorator to the function compute_square(n), which computes the square of a number and simulates a delay using time.sleep().
# Call the function compute_square(n).

### 🇺🇦 Ukrainian version:

# Тривалість роботи.

# Напишіть програму, яка створює декоратор для вимірювання часу виконання функції.
# Програма повинна:
# Визначити декоратор time_decorator, який вимірює та виводить час виконання функції.
# Застосувати декоратор до функції compute_square(n), яка обчислює квадрат числа та імітує затримку за допомогою time.sleep().
# Викликати функцію compute_square(n).

# Write your code here
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"The function {func.__name__} completed in {(t2 - t1):.5f}s")
        return result

    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(1)
    return n ** 2

compute_square(5)
