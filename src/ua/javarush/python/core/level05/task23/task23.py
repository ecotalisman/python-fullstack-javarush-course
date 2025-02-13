# Reverse Tuple

# Write a program that creates a tuple with an arbitrary number of elements entered by the user.
# Then, the program should print the tuple in reverse order using slicing.

### 🇺🇦 Ukrainian version:

# Зворотний кортеж

# Напишіть програму, яка створює кортеж з довільної кількості елементів, запитуваних у користувача.
# Потім програма повинна вивести кортеж у зворотному порядку з використанням зрізу.

# Write your code here
l = []
while True:
    el = input("Enter elements or 'stop': ")
    if el.lower() == "stop":
        break
    else:
        l.append(el)

print(tuple(l[::-1]))