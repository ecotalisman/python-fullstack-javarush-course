# Exception Repackaging

# Write a function validate_input that takes a string and checks
# that it is not empty and its length does not exceed 10 characters.
# If the string is empty, raise a ValueError with the message "Input cannot be empty".
# If the string is too long, raise a ValueError with the message "Input is too long".
# Then catch this exception and repackage it into a custom exception InputValidationError,
# preserving the original exception as the cause.

### 🇺🇦 Ukrainian version:

# Переупаковка винятку

# Напишіть функцію validate_input, яка приймає рядок і перевіряє,
# що він не порожній і що його довжина не перевищує 10 символів.
# Якщо рядок порожній, запустіть ValueError з повідомленням "Input cannot be empty".
# Якщо рядок занадто довгий, запустіть ValueError з повідомленням "Input is too long".
# Потім перехопіть це виняток і переупакуйте його у користувацький виняток InputValidationError, зберігши початковий виняток як причину.

# Write your code here

# Example of usage:
class InputValidationError(Exception):
    pass

def validate_input(value):
    try:
        if value == "":
            raise ValueError("Input cannot be empty")
        elif len(value) > 10:
            raise ValueError("Input is too long")
    except ValueError as e:
        raise InputValidationError(f"Validation failed: {e}") from e

try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.__cause__}")
