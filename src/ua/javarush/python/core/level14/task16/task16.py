# Asynchronous Context Manager for File Operations

# Use the aiofiles library to create an asynchronous context manager
# that opens a file, writes the string "Asynchronous write to file" into it, and then closes the file.

### 🇺🇦 Ukrainian version:

# АКМ для роботи з файлами

# Використовуйте бібліотеку aiofiles для створення асинхронного контекстного менеджера,
# який буде відкривати файл, записувати в нього рядок "Асинхронний запис у файл" і закривати файл.

# Write your code here
import asyncio, aiofiles

async def main():
    async with aiofiles.open("example.txt", "w") as f:
        await f.write("Асинхронний запис у файл")

asyncio.run(main())
