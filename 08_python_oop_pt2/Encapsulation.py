class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number    # Public
        self.__balance = balance                # Private (Encapsulation)

    # deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    # check balance (getter)
    def get_balance(self):
        return self.__balance


# Usage
acc1 = BankAccount(101, 500)
acc1.deposit(200)       # ✅ Deposited 200. New balance: 700
acc1.withdraw(100)      # ✅ Withdrew 100. New balance: 600
print(acc1.get_balance())  # ✅ 600

# Direct access not allowed
# print(acc1.__balance)   # ❌ Error
