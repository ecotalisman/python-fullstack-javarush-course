# Incorrect Parameter Specification

# The example shows code that incorrectly catches multiple exception types at once.
# Write the corrected version below.

### 🇺🇦 Ukrainian version:

# Неправильне вказання параметрів

# У прикладі наведено код, який неправильно перехоплює кілька типів виключень одночасно.
# Напишіть нижче виправлений варіант.

# Wrong version: multiple exceptions are caught incorrectly
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("An error occurred: enter only numbers, except zero.")

# Write your code here
# Corrected version: proper exception handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Error: you must enter a valid number.")
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
