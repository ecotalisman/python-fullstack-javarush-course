# Re-grouping

# Write a program that takes a string of several words separated by commas from the user.
# The program should:
# - Split the string into a list of words using the split() method.
# - Join this list of words into a single string using the join() method, separating the words with spaces.
# - Display the results of each operation.

### 🇺🇦 Ukrainian version:

# Перегрупування.

# Напишіть програму, яка приймає рядок з кількох слів, розділених комами, від користувача.
# Програма повинна:
# Розділити рядок на список слів, використовуючи метод split().
# Об'єднати цей список слів в один рядок, використовуючи метод join(), розділивши слова пробілами.
# Вивести результати кожної операції.

# Write your code here
text = input("Enter words separated by commas: ")
print(text)
parts = text.split(',')
print(parts)
joined_text = ' '.join(parts)
print(joined_text)