# Emptiness Check

# Write a program that creates several dictionaries with different numbers of elements.
# The program should:
# - Print the number of elements in each dictionary.
# - Check if each dictionary is empty and display an appropriate message.
# To check if a dictionary is empty, create a function named check_empty.

### 🇺🇦 Ukrainian version:

# Перевірка на порожнечу.

# Напишіть програму, яка створює кілька словників з різною кількістю елементів.
# Програма повинна:
# Вивести кількість елементів у кожному словнику.
# Перевірити, чи порожній кожен словник, і вивести відповідне повідомлення.
# Для перевірки порожнечі словника потрібно створити функцію check_empty

# Write your code here
def check_empty(my_dict, dict_name):
    length = len(my_dict)
    if length > 0:
        print(f"Dictionary {dict_name} has {length} items")
    else:
        print(f"Dictionary {dict_name} is empty")

male_info = {"name" : "John", "age" : 25, "city" : "London"}
female_info = {"name" : "Djoanna", "age" : 20, "city" : "Paris", "is_merried" : "no"}
product_info = {"product" : "apple", "weight" : 50}
empty_dict = {}

dicts = [
    ("male_info", male_info),
    ("female_info", female_info),
    ("product_info", product_info),
    ("empty_dict", empty_dict)
]

for name, length_dict in dicts:
    check_empty(length_dict, name)
