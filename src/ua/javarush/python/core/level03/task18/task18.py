# Counting Money

# Write a program that asks the user for numbers and sums them up until the user enters a negative number.
# Use a while loop and the break statement to stop input when a negative number is entered.

### 🇺🇦 Ukrainian version:
# Рахуємо гроші

# Напишіть програму, яка запитує у користувача числа та сумує їх, поки користувач не введе від'ємне число.
# Використовуйте цикл while та оператор break для завершення введення при від'ємному числі.

# Write your code here
total_sum = 0
while True:
    number = float(input("Enter a number (negative to stop): "))
    if number < 0:
        print("Number is Negative, stop!")
        break
    total_sum += number
    print(f"Total sum {total_sum}")
