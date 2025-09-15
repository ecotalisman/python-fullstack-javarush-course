# Using ThreadLocal

# Write a program that uses the ThreadLocal class
# to store data unique to each thread.

### 🇺🇦 Ukrainian version:

# Використання ThreadLocal

# Напишіть програму, яка використовує клас ThreadLocal
# для зберігання даних, унікальних для кожного потоку.

# Write your code here
import threading

my_data = threading.local()

def process():
    my_data.value = threading.current_thread().name
    print(f"Value in {threading.current_thread().name}: {my_data.value}")

threads = []
for i in range(3):
    t = threading.Thread(target=process)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
