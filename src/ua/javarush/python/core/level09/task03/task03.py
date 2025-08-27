# Rectangles

# Create a class Rectangle with a constructor that takes parameters width and height.
# Add a method area() that returns the area of the rectangle.
# Create an object of this class and calculate its area.

### 🇺🇦 Ukrainian version:

# Прямокутники.

# Створіть клас Rectangle з конструктором, який приймає параметри width та height.
# Додайте метод area(), який повертає площу прямокутника.
# Створіть об'єкт цього класу та обчисліть його площу.

# Write your code here
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

obj = Rectangle(2, 3)
print(obj.area())
