# Managing Tasks

# Write an asynchronous program that creates two tasks.
# The first task should wait 1 second and print "First task completed",
# the second task should wait 2 seconds and print "Second task completed".
# Use asyncio.create_task() to create the tasks and asyncio.run() to execute them.

### 🇺🇦 Ukrainian version:

# Управління задачами (Tasks)

# Напишіть асинхронну програму, яка створює дві задачі.
# Перше завдання має чекати 1 секунду і друкувати "Перше завдання завершено",
# друге завдання має чекати 2 секунди і друкувати "Друге завдання завершено".
# Використовуйте asyncio.create_task() для створення задач і asyncio.run() для їх виконання.

# Write your code here
import asyncio

async def say(what, delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say("Перше завдання завершено", 1))
    task2 = asyncio.create_task(say("Друге завдання завершено", 2))
    await task1
    await task2

asyncio.run(main())
