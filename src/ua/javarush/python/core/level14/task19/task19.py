# Using Multiprocessing

# Write a program that creates 4 parallel processes.
# Each process should print its name and the current process ID.
# Use the multiprocessing module.

### 🇺🇦 Ukrainian version:

# Використання багатопроцесорності

# Напишіть програму, яка створює 4 паралельні процеси.
# Кожен процес повинен друкувати своє ім'я та поточний ідентифікатор процесу.
# Використовуйте модуль multiprocessing.

# Write your code here
import multiprocessing as mp
import os

def worker(num):
    proc = mp.current_process()
    print(f"Worker arg: {num} | name: {proc.name} | pid: {os.getpid()}")

def main():
    processes = []
    for i in range(4):
        p = mp.Process(target=worker, args=(i,), name=f"Worker-{i}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
