# The Rounding Mathematician

# Write a program that asks the user for a float number and rounds it down (using math.floor()),
# up (using math.ceil()), and to the nearest integer (using round()).
# Display the results of all three rounding methods.

### 🇺🇦 Ukrainian version:

# Круглий математик

# Напишіть програму, яка запитує у користувача дійсне число і округлює його вниз (з використанням math.floor()),
# вгору (з використанням math.ceil()) та до найближчого цілого числа (з використанням round()).
# Виведіть результати всіх трьох округлень.

# Write your code here
import math

number = input("Enter float number: ")
print(math.floor(float(number)))
print(math.ceil(float(number)))
print(round(float(number)))