# The run() Method

# Write an asynchronous program that prints "Start",
# then pauses for 3 seconds, prints "In progress",
# then pauses again for 2 seconds and prints "End".
# Use the asyncio.run() method to launch the main coroutine.

### 🇺🇦 Ukrainian version:

# Метод run()

# Напишіть асинхронну програму, яка виводить на екран "Початок",
# потім робить паузу на 3 секунди, виводить "В процесі",
# знову робить паузу на 2 секунди і виводить "Кінець".
# Використайте метод asyncio.run() для запуску основної корутини.

# Write your code here
import asyncio

async def main():
    print("Початок")
    await asyncio.sleep(3)
    print("В процесі")
    await asyncio.sleep(2)
    print("Кінець")

asyncio.run(main())
