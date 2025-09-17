# Asynchronous Generator

# Write an asynchronous generator that generates numbers from 0 to 2
# with a delay of 1 second between numbers.
# Use this generator in an asynchronous function to print the values to the screen.

### 🇺🇦 Ukrainian version:

# Асинхронний генератор

# Напишіть асинхронний генератор, який буде генерувати числа від 0 до 2
# із затримкою в 1 секунду між числами.
# Використовуйте цей генератор в асинхронній функції, щоб вивести значення на екран.

# Write your code here
import asyncio


async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main():
    async for value in async_generator():
        print(value)


asyncio.run(main())
