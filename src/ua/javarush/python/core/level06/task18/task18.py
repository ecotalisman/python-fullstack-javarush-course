# Characters in a String

# Write a program that takes a string from the user, prints its length,
# then asks the user for an index.
# The program should print the character at that index in the string.
# If the index is out of range, the program should display an appropriate message.

### 🇺🇦 Ukrainian version:

# Символи в рядку

# Напишіть програму, яка приймає рядок від користувача, виводить його довжину,
# а потім запитує у користувача індекс.
# Програма повинна вивести символ рядка за цим індексом.
# Якщо індекс виходить за межі рядка, програма повинна вивести відповідне повідомлення.

# Write your code here
text = input("Enter the main string: ")
print(f"Length: {len(text)}")

index = int(input("Enter an index: "))

if 0 <= index < len(text):
    print(f"Character at index {index}: {text[index]}")
else:
    print("Index out of range.")