# Clever Raja

# Write a program that calculates how many grains of rice are on each square of a chessboard,
# where the first square has 1 grain, the second has 2 grains, the third has 4 grains, and so on.
# There are a total of 64 squares on the chessboard.
# Use a for loop and the range() function to iterate through the squares and the print() function to display the result.
# Example:
# For the first three squares, the program should output:
# Square 1: 1 grain
# Square 2: 2 grains
# Square 3: 4 grains
# ...

# Write your code here

### 🇺🇦 Ukrainian version:
# Хитрий радж

# Напишіть програму, яка обчислює, скільки зерен виявиться на кожній клітинці шахової дошки,
# якщо на першу клітинку кладеться 1 зернятко, на другу — 2 зернятка, на третю — 4 зернятка і так далі.
# Всього на шаховій дошці 64 клітинки.
# Використовуйте цикл for та функцію range() для ітерації по клітинкам і функцію print() для виводу результату.
# Приклад:
# Для перших трьох клітинок програма має вивести:
# Клітинка 1: 1 зерно
# Клітинка 2: 2 зерна
# Клітинка 3: 4 зерна
# ...

# Write your code here
for i in range(0, 64):
    if i == 0:
        print(f'Клітинка {i + 1}: {2 ** i} зерно')
    else:
        print(f'Клітинка {i + 1}: {2 ** i} зерна')
