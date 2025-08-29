# Polymorphism

# Create a base class Shape with a method area that returns the area of the shape.
# Then create child classes Circle and Rectangle that override the area method
# to calculate the area of their respective shapes.
# Use polymorphism to create a list of shapes and calculate their areas.

### 🇺🇦 Ukrainian version:

# Поліморфізм.

# Створіть базовий клас Shape з методом area, який буде повертати площу фігури.
# Потім створіть дочірні класи Circle та Rectangle, які будуть перевизначати метод area для розрахунку площі своїх фігур.
# Використовуйте поліморфізм, щоб створити список фігур та обчислити їх площі.

# Write your code here

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")


# Write your code here
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(area)