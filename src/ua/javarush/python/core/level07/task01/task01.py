# Dictionary

# Write a program that creates a dictionary with information about a person (e.g., name, age, and city) in three different ways:
# - Using curly braces {}.
# - Using the dict() function with a sequence of key-value pairs.
# - Using the dict() function with named arguments.
# The program should print all three dictionaries.

### 🇺🇦 Ukrainian version:

# Словник.

# Напишіть програму, яка створює словник з інформацією про людину (наприклад, ім'я, вік та місто) трьома різними способами:
# Використання фігурних дужок {}.
# Використання функції dict() з послідовністю пар ключ-значення.
# Використання функції dict() з іменованими аргументами.
# Програма має вивести всі три словники.

# Write your code here
person = {"name" : "John", "age" : 30, "city" : "London"}
print(person)

person2 = dict([("name", "Don"), ("age", 20), ("city", "Lviv")])
print(person2)

person3 = dict(name = "Doe", age = 25, city = "Kyiv")
print(person3)
