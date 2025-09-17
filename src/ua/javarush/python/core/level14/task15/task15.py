# Asynchronous Context Manager

# Write an asynchronous context manager that prints a message upon entering and exiting the context.
# Inside the context, perform an asynchronous delay of 2 seconds and print the message "Inside the context".

### 🇺🇦 Ukrainian version:

# Асинхронний контекстний менеджер

# Напишіть асинхронний контекстний менеджер, який буде друкувати повідомлення при вході та виході з контексту.
# Всередині контексту виконайте асинхронну затримку на 2 секунди та виведіть повідомлення "Всередині контексту".

# Write your code here
import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("Enter context")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exit context")


async def main():
    async with AsyncContextManager():
        await asyncio.sleep(2)
        print("Всередині контексту")

asyncio.run(main())
