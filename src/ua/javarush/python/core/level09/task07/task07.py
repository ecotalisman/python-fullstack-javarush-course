# Vehicles

# Create a base class Vehicle that has an attribute brand.
# Then create two child classes Car and Motorcycle that inherit from Vehicle
# and add their own unique attributes and methods.
# For example, the Car class may have a method drive, and the Motorcycle class may have a method ride.

### 🇺🇦 Ukrainian version:

# Машини.

# Створіть базовий клас Vehicle, який буде мати атрибут brand.
# Потім створіть два дочірніх класи Car і Motorcycle, які будуть наслідувати від Vehicle
# та додавати свої унікальні атрибути та методи.
# Наприклад, клас Car може мати метод drive, а клас Motorcycle — метод ride.

# Write your code here

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Write your code here
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving"


class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        return f"{self.brand} {self.model} is riding"


# Examples of using the classes:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla is driving.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 is riding.