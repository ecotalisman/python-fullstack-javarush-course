# Birthday
import datetime

# Write a program that asks the user for their date of birth (year, month, and day),
# and then prints the number of days that have passed from that date until today.
# The program should:
# - Ask the user for the year, month, and day of their birth.
# - Create a date object for the birthday using the datetime.date class.
# - Get the current date using the today() method.
# - Calculate the difference between the current date and the birthday.
# - Print the number of days that have passed since the birthday.

### 🇺🇦 Ukrainian version:

# День народження.

# Напишіть програму, яка запитує у користувача дату його народження (рік, місяць і день),
# а потім виводить кількість днів, що пройшли з цієї дати до сьогоднішнього дня.
# Програма повинна:
# Запитати у користувача рік, місяць і день його народження.
# Створити об'єкт дати народження за допомогою класу datetime.date.
# Отримати поточну дату за допомогою методу today().
# Обчислити різницю між поточною датою та датою народження.
# Вивести кількість днів, що пройшли з дати народження.

# Write your code here
import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

d = datetime.date(year, month, day)
today = datetime.date.today()

print(today - d)
