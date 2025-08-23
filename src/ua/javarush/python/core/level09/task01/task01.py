# Creating Objects

# Create a class Car with attributes make, model, and year.
# Add a method display_info() that prints information about the car.
# Then create an object of this class and call the display_info() method.

### 🇺🇦 Ukrainian version:

# Створюємо об'єкти.

# Створіть клас Car з атрибутами make, model і year.
# Додайте метод display_info(), який виводить інформацію про машину.
# Потім створіть об'єкт цього класу і викличте метод display_info().

# Write your code here
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(self.make, self.model, self.year)

bmw = Car("BMW", "X5", 2025)
bmw.display_info()
