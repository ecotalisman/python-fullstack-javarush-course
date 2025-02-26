# Detective

# Write a function set_detector that iterates through the list (or tuple) of its arguments
# and determines whether there is a set among them or not.
# Call the function set_detector with different parameter sets (with and without a set).

### 🇺🇦 Ukrainian version:

# Детектив

# Напиши функцію set_detector, яка проходиться по списку(кортежу) своїх аргументів і визначає - чи є серед них множина чи ні.
# Виклич функцію set_detector з різними варіантами параметрів (з множиною і без).

# Write your code here
def set_detector(*args):
    for arg in args:
        if isinstance(arg, set):
            print(f"{arg} has a Set!")
            return True
    print("No Set found!")
    return False

set_detector({1, 2, 3}, ["Aloe", "Vera"], "text")
set_detector([1, 2, 3], "hello", 20)
