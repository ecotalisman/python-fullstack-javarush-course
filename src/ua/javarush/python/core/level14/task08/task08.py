# Using Future

# Write an asynchronous function that takes a Future object
# and sets its result after a 1-second delay.
# Create an event loop, a Future object, and use the function to set the result.
# Then print the Future result on the screen.

### 🇺🇦 Ukrainian version:

# Використання Future

# Напишіть асинхронну функцію, яка приймає об'єкт Future
# і встановлює для нього результат після затримки у 1 секунду.
# Створіть цикл подій, об'єкт Future та використовуйте функцію для встановлення результату.
# Потім виведіть результат Future на екран.

# Write your code here
import asyncio

async def set_future(fut: asyncio.Future, value):
    await asyncio.sleep(1)
    fut.set_result(value)

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await set_future(fut, "Hello bro")
    print(fut.result())

asyncio.run(main())
