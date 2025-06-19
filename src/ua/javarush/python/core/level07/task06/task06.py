# Displaying Key-Value Pairs

# Write a program that creates a dictionary with information about a product (e.g., name, price, quantity).
# The program should:
# - Display all key-value pairs using the items() method.
# - Iterate over all key-value pairs and print them on the screen.
# - Add a new key-value pair to the dictionary and print all key-value pairs again.

### 🇺🇦 Ukrainian version:

# Відображення пар.

# Напишіть програму, яка створює словник з інформацією про продукт (наприклад, назва, ціна, кількість).
# Програма повинна:
# Вивести всі пари ключ-значення з використанням методу items().
# Ітерувати по всіх парах ключ-значення і вивести їх на екран.
# Додати нову пару ключ-значення у словник і знову вивести всі пари ключ-значення.

# Write your code here
product_dict = {"name" : "apple", "price" : 4, "quantity" : 100}
print(product_dict.items())
for key, value in product_dict.items():
    print(f"{key} : {value}")

product_dict.setdefault("weight", "50")
print(product_dict.items())
