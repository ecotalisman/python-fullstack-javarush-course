# The Fifth Element

# Write a program that creates a list with 5 elements entered by the user.
# The program should display the list, then ask the user for an element index and display the value of the element at that index.

### 🇺🇦 Ukrainian version:

# П'ятий елемент.

# Напишіть програму, яка створює список з 5 елементів, запитуваних у користувача.
# Програма повинна вивести список, потім запитати у користувача індекс елемента і вивести значення елемента за цим індексом.

# Write your code here
l = list(input("Enter element: ") for _ in range(5))
print(l)
n = int(input("Enter number of elements: "))
if 0 <= n < 5:
    print(l[n])
else:
    print("Number not found in the list")
