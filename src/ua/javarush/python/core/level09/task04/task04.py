# Banker

# Create a class BankAccount with a constructor that takes parameters account_number and initial_balance.
# Add a method deposit(amount) that adds funds to the account,
# and a method withdraw(amount) that withdraws funds from the account.
# Create an object of this class and perform several deposit and withdrawal operations.

### 🇺🇦 Ukrainian version:

# Банкір.

# Створіть клас BankAccount з конструктором, який приймає параметри account_number та initial_balance.
# Додайте метод deposit(amount), який поповнює рахунок, і метод withdraw(amount), який знімає кошти з рахунку.
# Створіть об'єкт цього класу та виконайте кілька операцій поповнення та зняття коштів.

# Write your code here
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            raise ValueError("Insufficient funds!")
        return self.balance


try:
    acc = BankAccount(1, 100)
    print(acc.deposit(1000))
    print(acc.withdraw(200))
    print(acc.withdraw(1000))
except ValueError as e:
    print(e)
