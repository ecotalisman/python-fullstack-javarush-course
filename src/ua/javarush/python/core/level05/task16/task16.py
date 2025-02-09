# Sorting Strings by Length

# Write a program that creates a list of 5 strings entered by the user.
# Then, the program should sort the list by string length and display the sorted list.

### 🇺🇦 Ukrainian version:

# Сортування рядків за довжиною

# Напишіть програму, яка створює список з 5 рядків, запитуваних у користувача.
# Потім програма повинна відсортувати список за довжиною рядків і вивести відсортований список.

# Write your code here
l = list(input("Add element: ") for n in range(5))
print(sorted(l, key=len))