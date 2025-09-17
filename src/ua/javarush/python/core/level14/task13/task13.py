# Using a Future object

# Write a program that creates a Future object and sets its result after 3 seconds.
# Use the set_result method to set the result and print the Future's result after it completes.

### 🇺🇦 Ukrainian version:

# Використання об'єкта Future

# Напиши програму, яка створює об'єкт Future і встановлює для нього результат через 3 секунди.
# Використай метод set_result для встановлення результату і виведи результат об'єкта Future після його завершення.

# Write your code here
import asyncio
from asyncio import Future

async def set_fut_result(fut: Future, delay):
    await asyncio.sleep(delay)
    fut.set_result("Result is ready Future")

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(set_fut_result(fut, 3))
    result = await fut
    print(result)

asyncio.run(main())
