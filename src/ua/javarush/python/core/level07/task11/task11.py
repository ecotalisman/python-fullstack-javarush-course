# Student Indexing

# Write a program that creates a dictionary with information about a student (name, age, university).
# The program should:
# - Iterate over the key-value pairs in the dictionary using the enumerate() function.
# - Print the index, key, and value of each pair.

### 🇺🇦 Ukrainian version:

# Індексація студентів.

# Напишіть програму, яка створює словник з інформацією про студента (ім'я, вік, університет).
# Програма повинна:
# Перебирати пари ключ-значення словника з використанням функції enumerate().
# Вивести індекс, ключ і значення кожної пари.

# Write your code here
stud_dict = {"name": "John", "age": 25, "University": "Harvard"}
for index, (key, value) in enumerate(stud_dict.items()):
    print(f"Index: {index}, Key: {key}, value: {value}")
