# You Say a Word, He Gives You a Reference

# Write a program that creates two lists, assigns one of them to another variable,
# and checks whether both variables refer to the same object.
# Use the 'is' operator to check the references.

### 🇺🇦 Ukrainian version:

# Ти йому слово, він тобі посилання

# Напишіть програму, яка створює два списки, присвоює один із них іншій змінній і перевіряє, чи вказують обидві змінні
# на один і той самий об'єкт.
# Використовуйте оператор is для перевірки посилань.

# Write your code here
a = [1, 2, 3]
b = a
if b is a:
    print("that's correct")