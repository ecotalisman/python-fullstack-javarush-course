# Extracting Information from an Exception
from sys import exception


# Write a function read_integer that takes a string and tries to convert it to an integer.
# If a ValueError occurs, handle the exception and print the error arguments and the error type.
# Additionally, save the exception in a variable and print it outside the except block.

### 🇺🇦 Ukrainian version:

# Витяг інформації з винятку

# Напишіть функцію read_integer, яка приймає рядок і намагається перетворити його на ціле число.
# Якщо виникає ValueError, обробіть виняток та виведіть аргументи помилки і тип помилки.
# Додатково, збережіть виняток у змінній і виведіть її за межами блока except.

# Write your code here
def read_integer(a):
    num_a = None
    exception = None
    try:
        num_a = int(a)
    except ValueError as e:
        exception = e
        print(f"Arguments of mistakes: {e.args}")
        print(f"Type of exception: {type(e)}")
        return exception
    return num_a or exception

print(read_integer("2"))
print(read_integer("a"))