# Variable Scope
from sys import exception


# Fix the code so that the last print raises an exception.

### 🇺🇦 Ukrainian version:

# Зона видимості змінної.

# Виправте код, щоб останній print виводив виняток.

# Write your code here

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)


def bad():
    try:
        bar(1)
    except KeyError as err:
        e = err
        print('key error')
    except ValueError as err:
        e = err
        print('value error')
    print(e)  # This should raise an my_exception because e is not defined in this scope.


bad()
