# Waiting for Stop

# Write a program that creates an empty list using square brackets [] and adds elements entered by the user.
# Input should continue until the user enters the word "stop". Then the program should display the final list.

### 🇺🇦 Ukrainian version:

# Очікування стопа

# Напишіть програму, яка створює пустий список за допомогою квадратних дужок [] і додає в нього елементи, запитувані у користувача.
# Введення елементів повинно продовжуватися доти, доки користувач не введе слово "стоп". Потім програма повинна вивести підсумковий список.

# Write your code here
my_list = []
while True:
    element = input("Add elements (or type 'стоп' to exit): ")
    if element.lower() == 'стоп':
        break
    my_list.append(element)

print(my_list)

