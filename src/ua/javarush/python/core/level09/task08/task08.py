# Shapes

# Create a base class Shape that has a method area for calculating the area.
# Then create two child classes Rectangle and Circle that inherit from Shape
# and override the area method to calculate the area of a rectangle and a circle, respectively.

### 🇺🇦 Ukrainian version:

# Фігури.

# Створіть базовий клас Shape, який буде мати метод area для обчислення площі.
# Потім створіть два дочірніх класи Rectangle і Circle, які будуть наслідувати від Shape
# і перевизначати метод area для обчислення площі прямокутника і кола відповідно.

# Write your code here


import math

class Shape:
    def area(self):
        pass

# Write your code here
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return self.a * self.b

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        super().area()
        return math.pi * self.r ** 2

# Example of usage:
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")