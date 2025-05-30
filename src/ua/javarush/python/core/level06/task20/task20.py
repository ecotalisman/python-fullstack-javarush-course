# Negative Slices

# Write a program that takes a string from the user and
# performs the following operations using negative indices and slicing:
# - Extracts the last three characters of the string.
# - Extracts the string excluding the last character.
# - Reverses the string.
# Print all three results.

### 🇺🇦 Ukrainian version:

# Від'ємні зрізи

# Напишіть програму, яка приймає рядок від користувача і
# виконує наступні операції з використанням від'ємних індексів та зрізів:
# Витягає останні три символи рядка.
# Витягає рядок, виключаючи останній символ.
# Перевертає рядок.
# Виводить всі три результати.

# Write your code here
text = input("Enter a string: ")

print(text[-3:])
print(text[:-1])
print(text[::-1])