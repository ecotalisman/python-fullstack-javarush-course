# Closure

# Write a program that creates a filter function using closures.
# The program should:
# Define an outer function make_filter(threshold) that creates and returns an inner function filter_func(value).
# The inner function filter_func(value) should return True if value is greater than threshold.
# Create several filter functions with different threshold values and
# use them to filter a list of data, printing the result to the screen.

### 🇺🇦 Ukrainian version:

# Замикання.

# Напишіть програму, яка створює функцію фільтра з використанням замикань.
# Програма повинна:
# Визначити зовнішню функцію make_filter(threshold), яка створює і повертає внутрішню функцію filter_func(value).
# Внутрішня функція filter_func(value) повинна повертати True, якщо value більше threshold.
# Створити декілька функцій фільтрів з різними пороговими значеннями і
# використовувати їх для фільтрації списку даних, виводячи результат на екран.

# Write your code here
def make_filter(threshold):
    def filter_func(value):
        return value > threshold
    return filter_func

filter_10 = list(filter(make_filter(10), [1, 2, 12, 20]))
print(filter_10)

filter_5 = list(filter(make_filter(5), [1, 2, 3, 5, 7, 9]))
print(filter_5)