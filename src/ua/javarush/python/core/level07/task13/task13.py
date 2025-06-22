# Dictionary Traversal

# Write a program that creates a dictionary with information about a person (e.g., name, age, address, and contact information).
# The program should:
# Traverse all elements of the dictionary, including nested dictionaries, using loops.
# Implement a function to traverse all levels of nesting and print keys and values.

### 🇺🇦 Ukrainian version:

# Обхід словника.

# Напишіть програму, яка створює словник з інформацією про людину (наприклад, ім'я, вік, адреса, та контактна інформація).
# Програма повинна:
# Перебрати всі елементи словника, включаючи вкладені словники, з використанням циклів.
# Реалізувати функцію для обходу всіх рівнів вкладеності та виводу ключів і значень.

# Write your code here
person = {
    "name": "John", "age": 20,
    "address": {
        "street": "205 Street",
        "zip": 20,
        "contact": {
            "e-mail": "info@gmail.com",
            "Tel.": 5552211
        }
    }
}


def print_dict(d, indent=0):
    for k, v in d.items():
        print(" " * indent + str(k) + ": ", end="")
        if isinstance(v, dict):
            print()
            print_dict(v, indent + 1)
        else:
            print(v)


print_dict(person)
