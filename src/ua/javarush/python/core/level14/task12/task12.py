# Cancelling a Task

# Write an asynchronous program that creates a task which waits for 5 seconds.
# Start it, wait 1 second, then cancel the task and print a message about its cancellation.
# Handle the CancelledError exception.

### 🇺🇦 Ukrainian version:

# Скасування задачі

# Напишіть асинхронну програму, яка створює задачу, що виконує очікування 5 секунд.
# Запустіть її, почекайте 1 секунду, потім скасуйте задачу і виведіть повідомлення про її скасування.
# Обробіть виняток CancelledError.

# Write your code here
import asyncio

async def main():
    t = asyncio.create_task(asyncio.sleep(5))
    await asyncio.sleep(1)
    t.cancel()
    try:
        await t
    except asyncio.CancelledError:
        print("Task was cancelled")


asyncio.run(main())
