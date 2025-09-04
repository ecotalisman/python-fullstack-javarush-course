# Custom Exception Hierarchy

# Create a base exception class ApplicationError and two subclasses NegativeValueError and ValueTooLargeError.
# Implement a function check_number that raises the appropriate exception
# if the number is negative or too large.
# Handle the exceptions in a try-except block.

### 🇺🇦 Ukrainian version:

# Ієрархія користувацьких виключень

# Створіть базовий клас виключень ApplicationError і два підкласи NegativeValueError та ValueTooLargeError.
# Реалізуйте функцію check_number, яка буде викликати відповідне виключення, якщо число від'ємне або занадто велике.
# Обробіть виключення в блоці try-except.

# Write your code here
class ApplicationError(Exception):
    pass

class NegativeValueError(ApplicationError):
    def __init__(self, value, message="Number must not be negative"):
        self.value = value
        super().__init__(f"{message}: {value}")

class ValueTooLargeError(ApplicationError):
    def __init__(self, value, upper=150, message="Number too large"):
        self.value = value
        self.upper = upper
        super().__init__(f"{message} (> {upper}): {value}")

def check_number(num, upper=150):
    if num < 0:
        raise NegativeValueError(num)
    elif num > upper:
        raise ValueTooLargeError(num, upper)

try:
    age = int(input("Enter your age: "))
    check_number(age)
    print("Age is valid")
except NegativeValueError as e:
    print(e)
except ValueTooLargeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age")
