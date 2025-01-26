# Mess

# Write a program that asks the user for an integer, a float, and a string.
# Then convert the integer to a float, the float to a string, and the string to an integer (if possible).
# Print the results of the conversions and their types.

### 🇺🇦 Ukrainian version:
# Каша

# Напишіть програму, яка запитує у користувача ціле число, дійсне число і рядок.
# Потім перетворіть ціле число в дійсне, дійсне число в рядок, і рядок в ціле число (якщо це можливо).
# Виведіть результати перетворень і їх типи.

# Write your code here
i = input("add int: ")
f = input("add float: ")
s = input("add str: ")

i = float(i)
f = str(f)
try:
    s = int(s)
except:
    "not int"

print(i, f, s)