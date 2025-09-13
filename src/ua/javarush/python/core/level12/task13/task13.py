# Creating and Deleting Directories

# Write a program that creates a new directory new_directory.
# Then create a nested directory parent_directory/child_directory.
# And then delete the created directories.

# Creating directory new_directory
# Write your code here

# Creating nested directory parent_directory/child_directory
# Write your code here

# Deleting directory new_directory
# Write your code here

# Deleting nested directory parent_directory/child_directory
# Write your code here


### 🇺🇦 Ukrainian version:

# Створення та видалення директорій

# Напишіть програму, яка створює нову директорію new_directory.
# Потім створює вкладену директорію parent_directory/child_directory.
# А потім видаляє створені директорії.

import os
import shutil

# Створення директорії new_directory
# Write your code here
os.mkdir('new_directory')

# Створення вкладеної директорії parent_directory/child_directory
# Write your code here
os.makedirs('parent_directory/child_directory')

# Видалення директорії new_directory
# Write your code here
os.rmdir('new_directory')

# Видалення вкладеної директорії parent_directory/child_directory
# Write your code here
path = os.path.join('parent_directory', 'child_directory')
os.removedirs(path)