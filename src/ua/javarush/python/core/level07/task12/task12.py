# Dictionary from Tuple List

# Write a program that creates a list of tuples with information about employees (e.g., name and position).
# The program should:
# - Use dictionary comprehension to create a dictionary from the list of tuples.
# - Print the created dictionary.

### 🇺🇦 Ukrainian version:

# Словник з переліку кортежів.

# Напишіть програму, яка створює перелік кортежів з інформацією про працівників (наприклад, ім'я та посада).
# Програма повинна:
# Використовувати dictionary comprehension для створення словника з переліку кортежів.
# Вивести створений словник.

# Write your code here
worker1 = [("John", "student")]
worker2 = [("Snow", "manager")]

worker_dict1 = {k: v for k, v in worker1}
worker_dict2 = {k: v for k, v in worker2}

workers = {**worker_dict1, **worker_dict2}
print(workers)