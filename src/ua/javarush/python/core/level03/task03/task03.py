# Height in Feet and Inches

# Write a program that converts the user's height from centimeters to feet and inches.
# The height value is stored in the variable `height_cm`. One inch equals 2.54 cm, and one foot equals 12 inches.
# Your task is to calculate the number of full feet in the given height and convert the remainder into inches.
# Print the result to the screen.

### 🇺🇦 Ukrainian version:
# Зріст у футах і дюймах

# Напишіть програму, яка переводить зріст користувача, заданий у сантиметрах, у футі та дюйми.
# Значення зросту задано у змінній height_cm. Один дюйм дорівнює 2.54 см, один фут дорівнює 12 дюймам.
# Ваше завдання — вирахувати кількість повних футів у даному зрості і залишок перевести в дюйми.
# Результат виведіть на екран.

height_cm = float(input("Введіть зріст у сантиметрах: "))

# Constants
cm_per_inch = 2.54
inch_per_foot = 12

# Write your code here
inches = height_cm / cm_per_inch
foot = inches // 12
residue_foot = inches % 12
print(foot, residue_foot)