# String Search

# Write a program that creates a list with 10 elements.
# The program asks the user to enter a string and then checks if it exists in the list.

### 🇺🇦 Ukrainian version:

# Пошук рядка

# Напишіть програму, яка створює список з 10 елементів.
# Програма просить користувача ввести рядок, а потім перевіряє - чи є він у списку.

# Write your code here
l = [1, 2, 3, 4, 5, "apple", "banana", "cherry", "a", "b"]
el = input("Add element to check: ")

if el.isdigit():
    el = int(el)

if el in l:
    print("Element is in the list!")
else:
    print("Element isn't in the list!")