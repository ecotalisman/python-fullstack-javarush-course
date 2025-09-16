# Creating and Executing Asynchronous Functions

# Write a program that creates and executes multiple asynchronous functions,
# each of which uses the await operator to wait for another asynchronous function to complete.

### 🇺🇦 Ukrainian version:

# Створення та виконання асинхронних функцій

# Напишіть програму, яка створює та виконує кілька асинхронних функцій,
# кожна з яких використовує оператор await для очікування завершення іншої асинхронної функції.

# Write your code here
import asyncio

async def async_sum(a, b):
    return a + b

async def async_mul(a, b):
    return a * b

async def main():
    task1 = await async_sum(5, 10)
    task2 = await async_mul(5, 5)
    print("Results:", task1, task2)

asyncio.run(main())
