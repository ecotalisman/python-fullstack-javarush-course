# Motor Pool

# Write a function check_subclass to check whether one class is a subclass of another.
# Use the issubclass() function to perform the check.
# Then create classes Vehicle, Car, and Bicycle, and check whether Car and Bicycle are subclasses of Vehicle.

### 🇺🇦 Ukrainian version:

# Автопарк.

# Напишіть функцію check_subclass для перевірки, чи є один клас підкласом іншого.
# Використовуйте функцію issubclass() для виконання перевірки.
# Потім створіть класи Vehicle, Car, Bicycle, і перевірте, чи є Car і Bicycle підкласами Vehicle.

# Write your code here
class Vehicle():
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

def check_subclass(cls_1, cls_2):
    return print(issubclass(cls_1, cls_2))

check_subclass(Car, Vehicle)
check_subclass(Bicycle, Vehicle)
