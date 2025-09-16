# Running Multiple Tasks in Parallel

# Write a program that uses asyncio.gather()
# to run multiple asynchronous tasks in parallel
# and collect their results.

### 🇺🇦 Ukrainian version:

# Виконання декількох завдань паралельно

# Напишіть програму, яка використовує asyncio.gather()
# для виконання декількох асинхронних завдань паралельно
# та збирає їх результати.

# Write your code here
import asyncio

async def task1(a, b):
    await asyncio.sleep(1)
    return a + b

async def task2(a, b):
    await asyncio.sleep(2)
    return a * b

async def main():
    results = await asyncio.gather(task1(5, 10), task2(5, 5))
    print(results)

asyncio.run(main())
