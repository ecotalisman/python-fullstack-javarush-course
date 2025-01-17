# Ternary Operator

# Write a program that asks the user for a number and uses the ternary operator to check if it is even or odd.
# Print the corresponding message.

### 🇺🇦 Ukrainian version:
# Тернарний оператор

# Напишіть програму, яка запитує у користувача число і використовує тернарний оператор для перевірки, чи є воно парним або непарним.
# Виведіть відповідне повідомлення.

# Write your code here
number = int(input("add number: "))
message = "even" if number % 2 == 0 else "odd"
print(message)