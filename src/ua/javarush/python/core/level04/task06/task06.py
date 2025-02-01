# Random Average

# Write a program that generates 10 random numbers in the range from 1 to 100 using the random library.
# Then calculate their average and display it on the screen.

### 🇺🇦 Ukrainian version:

# Випадковий середнячок

# Напишіть програму, яка генерує 10 випадкових чисел у діапазоні від 1 до 100, використовуючи бібліотеку random.
# Потім обчисліть їх середнє значення і виведіть його на екран.

# Напишіть тут ваш код
from random import randint as r
import statistics

array = [(r(1, 100)) for i in range(10)]

print(statistics.mean(array))
