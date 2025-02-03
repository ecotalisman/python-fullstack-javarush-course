# VAT

# Write a function calculate_total_cost(price, tax=0.2) that takes the price of an item and an optional tax parameter (default is 20%).
# The function should calculate and print the total cost of the item including tax.
# Then write a program that calls this function with different parameters.

### 🇺🇦 Ukrainian version:

# ПДВ

# Напишіть функцію calculate_total_cost(price, tax=0.2), яка приймає ціну товару та необов'язковий параметр податок (за замовчуванням 20%).
# Функція повинна обчислювати і виводити загальну вартість товару з урахуванням податку.
# Потім напишіть програму, яка викликає цю функцію з різними параметрами.

# Write your code here
def calculate_total_cost(price, tax=0.2):
    return print(float(price * (1 + tax)))

calculate_total_cost(100)
calculate_total_cost(100, 0.25)
calculate_total_cost(50)