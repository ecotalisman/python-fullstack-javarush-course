# Comparing is Very Simple

# Write a program that asks the user for two float numbers and compares them using an acceptable epsilon margin of error.
# Display the comparison result on the screen.

### 🇺🇦 Ukrainian version:

# Порівнювати дуже просто

# Напишіть програму, яка запитує у користувача два дійсних числа і порівнює їх з використанням допустимої похибки epsilon.
# Виведіть результат порівняння на екран.

# Write your code here
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
epsilon = 0.00001

if  abs(a - b) < epsilon:
    print("equals")
else:
    print("not equals")
