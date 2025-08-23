# Infinite Number of Names

# Write a program that takes any number of named arguments and prints information about a person.
# The program should:
# Define a function print_person_info(**kwargs) that accepts any number of named arguments.
# Print each argument name and its value.

### 🇺🇦 Ukrainian version:

# Нескінченна кількість імен.

# Напишіть програму, яка приймає довільну кількість іменованих аргументів і виводить інформацію про людину.
# Програма повинна:
# Визначити функцію print_person_info(**kwargs), яка приймає довільну кількість іменованих аргументів.
# Вивести кожне ім'я аргументу та його значення.

# Write your code here
def print_person_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_person_info(name="John", age=20, city="London")