# The Unknown

# Write a program that asks the user for two numbers.
# If the user does not enter a value (leaves it blank), use the default value None for that number.
# Calculate and display the sum of these numbers.

### 🇺🇦 Ukrainian version:

# Невідомість

# Напишіть програму, яка запитує у користувача два числа.
# Якщо користувач не вводить значення (порожній рядок), використовуйте значення за замовчуванням None для цього числа.
# Обчисліть і виведіть суму цих чисел.

# Write your code here
a, b = input("Enter number one: ") or None, input("Enter number two: ") or None
if a is None or b is None:
    print("Сума чисел невідома")
else:
    print("Sum = ", int(a) + int(b))