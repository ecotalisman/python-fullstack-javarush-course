# In the Depths of Depths

# Write a program that creates a dictionary with information about a person (e.g., name, age, address, and contact information).
# The program should:
# Modify a top-level value, a nested dictionary, and a deeper level of nesting.
# Add a new element to a nested dictionary.
# Delete an element from a nested dictionary and from the top level.

### 🇺🇦 Ukrainian version:

# У глибинах самих глибин.

# Напишіть програму, яка створює словник з інформацією про людину (наприклад, ім'я, вік, адреса, і контактна інформація).
# Програма повинна:
# Змінити значення верхнього рівня, вкладеного словника і більш глибокого рівня вкладеності.
# Додати новий елемент у вкладений словник.
# Видалити елемент із вкладеного словника і верхнього рівня.

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

person["name"] = "Snow"
person["address"]["street"] = "200 Street"
person["address"]["contact"]["Tel."] = 4442211
person["address"]["apartment"] = 15

del person["age"]
del person["address"]["zip"]
print(person)