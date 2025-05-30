# Cleaning

# Write a program that takes a string from the user and performs the following operations:
# - Removes leading and trailing spaces using the strip() method.
# - Converts all characters in the string to lowercase using the lower() method.
# - Converts all characters in the string to uppercase using the upper() method.
# Display the result of each operation.

### 🇺🇦 Ukrainian version:

# Очищення

# Напишіть програму, яка приймає рядок від користувача і виконує наступні операції:
# Видаляє пробіли на початку і в кінці рядка з використанням методу strip().
# Перетворює всі символи рядка в нижній регістр з використанням методу lower().
# Перетворює всі символи рядка у верхній регістр з використанням методу upper().
# Виводить результати кожної операції.

# Write your code here
text = input("Enter a string: ")

stripped_text = text.strip()
print(f"After strip(): {stripped_text}")

lower_text = stripped_text.lower()
print(f"After lower(): {lower_text}")

upper_text = stripped_text.upper()
print(f"After upper(): {upper_text}")
