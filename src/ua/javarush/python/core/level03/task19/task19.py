# F-Notation

# Write a program that asks the user for their name, age, and city.
# Then use f-string notation to display a message in the following format:
# "Hello, {name}! You are {age} years old, and you live in {city}."

### 🇺🇦 Ukrainian version:
# F-нотація

# Напишіть програму, яка запитує у користувача його ім'я, вік та місто.
# Потім використайте f-нотацію, щоб вивести повідомлення у наступному форматі: "Привіт, {ім'я}! Тобі {вік} років, і ти живеш у місті {місто}."

# Write your code here
name = input("Add your name: ")
age = int(input("Add your age: "))
city = input("Add your city: ")
print(f"Привіт, {name}! Тобі {age} років, і ти живеш у місті {city}.")