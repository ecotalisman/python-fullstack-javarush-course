# Adding an Element

# Write a program that creates a tuple with 5 elements entered by the user.
# Then, the program should ask the user for a new element and add it to the end of the tuple, creating a new tuple.
# The program should display the updated tuple.

### 🇺🇦 Ukrainian version:

# Додавання елемента

# Напишіть програму, яка створює кортеж з 5 елементів, що запитуються у користувача.
# Потім програма повинна запросити у користувача новий елемент і додати його в кінець кортежу, створюючи новий кортеж.
# Програма повинна вивести оновлений кортеж.

# Write your code here
t = tuple([input("Enter elements: ") for _ in range(5)])
l = list(t)
l.append(input("Enter a new elements: "))
t = tuple(l)
print(t)