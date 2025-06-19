# Three Ways to Dig into a Dictionary

# Write a program that creates a dictionary with information about a person.
# The program should:
# - Retrieve a value by key using square brackets.
# - Safely retrieve a value by key using the get() method.
# - Use the setdefault() method to get a value by key and add the key if it is missing.

### 🇺🇦 Ukrainian version:

# Три способи порпатися в словнику.

# Напишіть програму, яка створює словник з інформацією про людину.
# Програма повинна:
# Отримати значення за ключем з використанням квадратних дужок.
# Безпечно отримати значення за ключем з використанням методу get().
# Використовувати метод setdefault() для отримання значення за ключем та додавання ключа, якщо він відсутній.

# Write your code here
person = {"name" : "John", "age" : 25, "city" : "London"}
print(person["name"])
print(person.get("age"))
print(person.setdefault("work", "ASC"))