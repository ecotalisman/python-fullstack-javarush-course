# Using the Timer class

# Write a program that uses the Timer class
# to execute a function with a delay
# and demonstrates canceling the timer before it triggers.

### 🇺🇦 Ukrainian version:

# Використання класу Timer

# Напишіть програму, яка використовує клас Timer
# для виконання функції з затримкою
# та демонструє скасування таймера до його спрацювання.

# Write your code here
import threading

def hello():
    print("Hello")

t = threading.Timer(3, hello)
t.start()
t.cancel()
