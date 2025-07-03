# Generator

# Write a program that creates a counter generator function using closures.
# The program should:
# Define an outer function make_counter() that creates and returns an inner function counter().
# The inner function counter() should increment the counter value and return it.
# Create several independent counters and call them multiple times, printing the result.

### 🇺🇦 Ukrainian version:

# Генератор.

# Напишіть програму, яка створює функцію-генератор лічильника з використанням замикань.
# Програма повинна:
# Визначити зовнішню функцію make_counter(), яка створює та повертає внутрішню функцію counter().
# Внутрішня функція counter() повинна збільшувати значення лічильника та повертати його.
# Створити декілька незалежних лічильників і викликати їх кілька разів, виводячи результат на екран.

# Write your code here
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counter = make_counter()
print(counter())
print(counter())
print(counter())

other_counter = make_counter()
print(other_counter())
print(other_counter())
print(other_counter())

