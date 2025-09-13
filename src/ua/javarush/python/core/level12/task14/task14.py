# Listing Files and Directories

# Write a program that prints the contents of the current working directory and
# for each file or directory specifies whether it is a file or a directory.
# Write your code here


### 🇺🇦 Ukrainian version:

# Отримання списку файлів і директорій

# Напишіть програму, яка виводить вміст поточної робочої директорії та
# для кожного файлу або директорії вказує, чи є це файлом або директорією.
# Напишіть тут ваш код
import os

with os.scandir('.') as entries:
    for entry in entries:
        print(f"Name: {entry.name}, Directory: {entry.is_dir()}, File: {entry.is_file()}")
