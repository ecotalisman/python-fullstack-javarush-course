# Handling Future Exceptions

# Write a program that creates a Future object and sets an exception for it after 2 seconds.
# Use the set_exception method to set the exception and handle this exception once it occurs.

### 🇺🇦 Ukrainian version:

# Обробка виключень Future

# Напишіть програму, яка створює об'єкт Future і встановлює для нього виключення через 2 секунди.
# Використовуйте метод set_exception для встановлення виключення і обробіть це виключення після його виникнення.

# Write your code here
import asyncio
from asyncio import Future

async def set_fut_except(fut: Future, delay):
    await asyncio.sleep(delay)
    fut.set_exception(ValueError("There was an error"))

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(set_fut_except(fut, 2))
    try:
        result = await fut
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Success: {result}")

asyncio.run(main())
