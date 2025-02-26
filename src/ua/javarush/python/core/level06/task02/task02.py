# Unique List

# Write a program that creates a list with 10 elements entered by the user.
# Then, the program should create a set from the list elements to keep only unique elements and display the resulting set.

### 🇺🇦 Ukrainian version:

# Унікальний список.

# Напишіть програму, яка створює список з 10 елементів, запитуваних у користувача.
# Потім програма повинна створити множину з елементів списку, щоб залишити лише унікальні елементи, і вивести отриману множину.

# Write your code here
l = [input("Add elements: ") for _ in range(10)]
s = set(l)
print(s)