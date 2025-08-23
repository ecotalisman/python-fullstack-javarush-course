# Timezone

# Write a program that converts the current time from the UTC timezone to a user-specified timezone.
# The program should:
# - Get the current time in the UTC timezone.
# - Ask the user for the offset in hours relative to UTC.
# - Create a timezone object with the specified offset.
# - Convert the current time to the specified timezone.
# - Print the current time in both UTC and the specified timezone.

### 🇺🇦 Ukrainian version:

# Timezone.

# Напишіть програму, яка конвертує поточний час із часового поясу UTC у заданий користувачем часовий пояс.
# Програма повинна:
# Отримати поточний час у часовому поясі UTC.
# Запросити у користувача зміщення в годинах відносно UTC.
# Створити об'єкт часового поясу із заданим зміщенням.
# Конвертувати поточний час у заданий часовий пояс.
# Вивести поточний час у UTC і у заданому часовому поясі.

# Write your code here
from datetime import datetime, timedelta, timezone

dt_utc = datetime.now(timezone.utc)
other = float(input("Add hours: "))
tz = timezone(timedelta(hours=other))
dt_user = dt_utc.astimezone(tz)

print("UTC:", dt_utc.strftime("%Y-%m-%d %H:%M:%S %z"))
print(f"UTC{other:+g}:", dt_user.strftime("%Y-%m-%d %H:%M:%S %z"))
