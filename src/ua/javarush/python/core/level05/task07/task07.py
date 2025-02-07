# Who Wants More?

# Write a program that creates an empty list, then asks the user for 5 elements and adds them to the list using the append() method.
# After that, the program should display the final list.

### 🇺🇦 Ukrainian version:

# Хто хоче добавки?

# Напишіть програму, яка створює порожній список, потім запитує у користувача 5 елементів і додає їх до списку за допомогою методу append().
# Після цього програма повинна вивести підсумковий список.

# Write your code here
l = []
for _ in range(5):
    el = input("Add an elements to the list: ")
    l.append(el)
print(l)