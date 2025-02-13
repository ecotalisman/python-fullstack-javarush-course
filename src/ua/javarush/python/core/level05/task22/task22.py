# Tuple Index

# Write a program that creates a tuple with 5 elements entered by the user.
# Then, the program should ask the user for an element index and print the value at that index.
# If the index is out of range, the program should display an appropriate message.

### 🇺🇦 Ukrainian version:

# Номер кортежу

# Напишіть програму, яка створює кортеж з 5 елементів, запитуваних у користувача.
# Потім програма повинна запитати у користувача індекс елемента і вивести значення елемента за цим індексом.
# Якщо індекс виходить за межі кортежу, програма повинна вивести відповідне повідомлення.

# Write your code here
l = list(input("Enter elements: ") for l in range(5))

t = tuple(l)

i = int(input("Enter the index in the tuple: "))
print(t[i]) if -len(t) <= i < len(t) else print("Error: Index out of range")
