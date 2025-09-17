# Managing the Event Loop

# Write an asynchronous program that creates two tasks.
# The first task should print "First task" and wait for 2 seconds,
# the second task should print "Second task" and wait for 3 seconds.
# Use asyncio.create_task() to create the tasks and run them in parallel, waiting for both to finish.

### 🇺🇦 Ukrainian version:

# Управління циклом подій

# Напишіть асинхронну програму, яка створює дві задачі.
# Перша задача має друкувати "Перша задача" і чекати 2 секунди,
# друга задача має друкувати "Друга задача" і чекати 3 секунди.
# Використовуйте asyncio.create_task() для створення задач та виконуйте їх паралельно, дочекавшись завершення обох.

# Write your code here
import asyncio

async def worker(msg, delay):
    print(msg)
    await asyncio.sleep(delay)

async def main():
    t1 = asyncio.create_task(worker("Перша задача", 2))
    t2 = asyncio.create_task(worker("Друга задача", 3))
    await asyncio.gather(t1, t2)


asyncio.run(main())
