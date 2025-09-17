# Creating and Getting the Event Loop

# Write a program that creates a new event loop,
# sets it as the current one, and prints it.
# Then create another new event loop and set it as the current one again.
# Make sure you are switching event loops correctly.

### 🇺🇦 Ukrainian version:

# Створення та отримання циклу подій

# Напишіть програму, яка створює новий цикл подій,
# встановлює його як поточний та друкує його.
# Потім створіть ще один новий цикл подій і знову встановіть його як поточний.
# Переконайтеся, що ви правильно змінюєте цикли подій.

# Write your code here
import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
print(asyncio.get_event_loop())

new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)
print(asyncio.get_event_loop())

loop.close()
new_loop.close()
