# Asynchronous Programming

# Write an asynchronous program that runs 30 tasks in parallel.
# Each task should wait for 2 seconds and then print its message "Task n done", where n is the task number.
# Use the asyncio module.

### 🇺🇦 Ukrainian version:

# Асинхронне програмування

# Напишіть асинхронну програму, яка виконує 30 задач паралельно.
# Кожна задача має очікувати 2 секунди і потім виводити своє повідомлення "Task n done", де n - номер задачі.
# Використайте модуль asyncio.

# Write your code here
import asyncio


async def worker(n):
    await asyncio.sleep(2)
    print(f"Task {n} done")


async def main():
    async with asyncio.TaskGroup() as tg:
        for n in range(1, 31):
            tg.create_task(worker(n))


asyncio.run(main())
