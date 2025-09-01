# Getting a Number

# Write a function process_input that takes a string and tries to convert it into an integer.
# If the conversion is successful, the function should return the square of the number.
# If the string is not a number, handle ValueError and print an error message.
# If the string is empty, handle IndexError and print an appropriate message.

### 🇺🇦 Ukrainian version:

# Отримання числа.

# Напишіть функцію process_input, яка приймає рядок і намагається перетворити його в ціле число.
# Якщо перетворення успішне, функція повинна повертати квадрат числа.
# Якщо рядок не є числом, обробіть ValueError і виведіть повідомлення про помилку.
# Якщо рядок порожній, обробіть IndexError і виведіть відповідне повідомлення.

# Write your code here
def process_input(string):
    try:
        if string == "":
            raise IndexError("Empty string")
        num = int(string)
        return num ** 2
    except ValueError:
        return "Помилка: введений рядок не є числом."
    except IndexError:
        return "Помилка: введено порожній рядок."

# Examples of function calls
print(process_input("5"))         # Вивід: 25
print(process_input("abc"))       # Вивід: Помилка: введений рядок не є числом.
print(process_input(""))          # Вивід: Помилка: введено порожній рядок.
