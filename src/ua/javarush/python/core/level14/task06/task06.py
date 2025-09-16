# The sleep() Method

# Write an asynchronous function that takes a string and a delay in seconds,
# then prints the string after the specified delay.
# Create two tasks, each calling this function with different strings and delays.
# Run them simultaneously using the asyncio.run() method.

### 🇺🇦 Ukrainian version:

# Метод sleep()

# Напишіть асинхронну функцію, яка приймає рядок і затримку в секундах,
# потім виводить рядок після вказаної затримки.
# Створіть дві задачі, кожна з яких викликає цю функцію
# з різними рядками і затримками.
# Запустіть їх одночасно, використовуючи метод asyncio.run().

# Write your code here
import asyncio

async def say(what, delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say("Hello", 1))
    task2 = asyncio.create_task(say("bro", 2))
    await asyncio.gather(task1, task2)

asyncio.run(main())
