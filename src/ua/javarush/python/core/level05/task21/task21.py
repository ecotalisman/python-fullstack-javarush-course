# User Tuple

# Write a program that creates a tuple with an arbitrary number of elements entered by the user.
# Then, the program should print the last element of the tuple.
# If the tuple is empty, the program should display a message indicating this.

### 🇺🇦 Ukrainian version:

# Кортеж користувача

# Напишіть програму, яка створює кортеж з довільної кількості елементів, запитуваних у користувача.
# Потім програма має вивести останній елемент кортежу.
# Якщо кортеж порожній, програма має вивести повідомлення про це.

# Write your code here
l = []
while True:
    el = input("Enter elements or 'stop': ")
    if el.lower() == "stop":
        break
    else:
        l.append(el)

t = tuple(l)

if t:
    print(t[-1])
else:
    print("Empty tuple()")