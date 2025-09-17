# Starting and Stopping the Event Loop

# Write a program that runs the event loop in infinite mode.
# Schedule stopping the loop after 3 seconds using the call_later method.
# Print the state of whether the loop is running before and after calling the stop() method.

### 🇺🇦 Ukrainian version:

# Запуск і зупинка циклу подій

# Напишіть програму, яка запускає цикл подій у безкінечному режимі.
# Заплануйте зупинку циклу через 3 секунди, використовуючи метод call_later.
# Виведіть стан, чи запущений цикл, до і після виклику методу stop().

# Write your code here
import asyncio
from asyncio import AbstractEventLoop

def my_callback(loop: AbstractEventLoop):
    print("Callback executed after delay")
    loop.stop()

loop = asyncio.new_event_loop()
loop.call_later(3, my_callback, loop)

print("Loop running?", loop.is_running())
loop.run_forever()
print("Loop running?", loop.is_running())
