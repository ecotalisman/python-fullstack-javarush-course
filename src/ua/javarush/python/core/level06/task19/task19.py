# Extracting Substrings

# Write a program that takes a string from the user and extracts substrings using slicing.
# The program should:
# - Extract a substring from the 3rd to the 8th character (inclusive).
# - Extract a substring from the 5th character to the end of the string.
# Then print both substrings.

### 🇺🇦 Ukrainian version:

# Витягування підрядків.

# Напишіть програму, яка приймає рядок від користувача та витягує з нього підрядки, використовуючи зрізи.
# Програма повинна:
# Витягнути підрядок з 3-го по 8-й символ (індекс) включно.
# Витягнути підрядок з 5-го символу (індексу) до кінця рядка.
# Вивести обидва підрядки.

# Write your code here
text = input("Enter a string (minimum 10 characters): ")
while len(text) < 10:
    print("The string is too short. Please try again.")
    text = input("Enter a string (minimum 10 characters): ")

subString1 = text[2:9]
subString2 = text[4:]

print(subString1)
print(subString2)