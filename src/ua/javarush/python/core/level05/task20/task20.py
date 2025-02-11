# Unpacking

# Write a program that creates a tuple with 3 elements (for example, name, age, city).
# Then, the program should unpack the tuple into separate variables and print each variable.

### 🇺🇦 Ukrainian version:

# Розпакування

# Напишіть програму, яка створює кортеж з 3 елементів (наприклад, ім'я, вік, місто).
# Потім програма повинна розпакувати кортеж в окремі змінні і вивести кожну змінну.

# Write your code here
t = ("Alice", 30, "New York")
name, age, city = t
print(name, age, city, sep="\n")