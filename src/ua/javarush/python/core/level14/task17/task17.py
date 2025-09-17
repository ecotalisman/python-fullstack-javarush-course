# Asynchronous Iterator

# Write an asynchronous iterator that returns numbers from 1 to 5
# with a delay of 1 second between numbers.
# Use this iterator in an asynchronous function to print the numbers to the screen.

### 🇺🇦 Ukrainian version:

# Асинхронний ітератор

# Напишіть асинхронний ітератор, який буде повертати числа від 1 до 5
# із затримкою в 1 секунду між числами.
# Використайте цей ітератор в асинхронній функції, щоб вивести числа на екран.

# Write your code here
import asyncio


class AsyncIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current > self.end:
            raise StopAsyncIteration

        await asyncio.sleep(1)
        value = self.current
        self.current += 1
        return value


async def main():
    async for number in AsyncIterator(1, 5):
        print(number)


asyncio.run(main())
