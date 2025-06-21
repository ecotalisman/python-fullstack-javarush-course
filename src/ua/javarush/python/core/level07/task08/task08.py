# Ivy League

# Write a program that creates a dictionary with information about a student (name, age, university).
# The program should:
# - Check for the value "MIT" using the values() method.
# - Check for the value "Harvard" using the set() function.
# - Check for the value 22 using a generator expression.

### 🇺🇦 Ukrainian version:

# Ліга Плюща

# Напишіть програму, яка створює словник з інформацією про студента (ім'я, вік, університет).
# Програма повинна:
# Перевірити наявність значення "MIT" з використанням методу values().
# Перевірити наявність значення "Harvard" з використанням функції set().
# Перевірити наявність значення 22 з використанням генератора.

# Write your code here
student_dict = {"ім'я": "John", "вік": 22, "університет": "Harvard"}

if "MIT" in student_dict.values():
    print("The value 'MIT' is present in the dictionary")
else:
    print("The value 'MIT' isn't present in the dictionary")

values_set = set(student_dict.values())
if "Harvard" in values_set:
    print("The value 'Harvard' is present in the dictionary")
else:
    print("The value 'Harvard' isn't present in the dictionary")

if  any(value == 22 for value in student_dict.values()):
    print("The value 22 is present in the dictionary")
else:
    print("The value 22 isn't present in the dictionary")

