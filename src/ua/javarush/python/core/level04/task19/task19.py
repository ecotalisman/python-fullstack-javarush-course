# Using a Global Variable

# Write a program with a global variable counter set to 0.
# Write a function increment_counter() that increases the value of this variable by 1 each time it is called.
# Then call this function several times and print the value of the global variable counter.

### 🇺🇦 Ukrainian version:

# Використання глобальної змінної

# Напишіть програму, у якій є глобальна змінна counter, що дорівнює 0.
# Напишіть функцію increment_counter(), яка збільшує значення цієї змінної на 1 кожен раз, коли вона викликається.
# Потім викличте цю функцію кілька разів і виведіть значення глобальної змінної counter.

# Write your code here
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print(increment_counter())
print(increment_counter())
print(increment_counter())

