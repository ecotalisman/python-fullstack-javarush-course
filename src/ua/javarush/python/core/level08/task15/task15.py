# Working with Directories

# Write a program that creates a directory, navigates into it, creates a file inside this directory,
# writes text to the file, and then reads and prints its content.
# The program should:
# - Create a directory named test_directory.
# - Navigate into the test_directory.
# - Create a file test_file.txt and write the string "Hello, World!" to it.
# - Read the content of test_file.txt and print it to the screen.
# - Delete the file and the directory.

### 🇺🇦 Ukrainian version:

# Робота з директоріями.

# Напишіть програму, яка створює директорію, переходить у неї, створює файл всередині цієї директорії,
# записує в файл текст, а потім читає та виводить його вміст.
# Програма повинна:
# Створити директорію test_directory.
# Перейти в директорію test_directory.
# Створити файл test_file.txt і записати в нього рядок "Hello, World!".
# Прочитати вміст файлу test_file.txt і вивести його на екран.
# Видалити файл і директорію.

# Write your code here
import os

if not os.path.exists("test_directory"):
    os.mkdir("test_directory")

os.chdir("test_directory")
with open("test_file.txt", "w") as f:
    f.write("Hello, World!")

with open("test_file.txt", "r") as f:
    print(f.read())

os.remove("test_file.txt")
os.chdir("..")
os.rmdir("test_directory")
