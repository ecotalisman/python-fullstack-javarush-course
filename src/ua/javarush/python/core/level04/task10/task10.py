# Leap Year

# Write a program that asks the user for a year and checks if it is a leap year.
# Use logical operators to verify the leap year conditions.
# A leap year is divisible by 4 but not divisible by 100, except for years that are divisible by 400.

### 🇺🇦 Ukrainian version:

# Високосний рік

# Напишіть програму, яка запитує у користувача рік і перевіряє, чи є він високосним.
# Використовуйте логічні оператори для перевірки умов високосного року.
# Високосний рік ділиться на 4, але не ділиться на 100, за винятком років, які діляться на 400.

# Write your code here
year = int(input("Enter your year of birth: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")
