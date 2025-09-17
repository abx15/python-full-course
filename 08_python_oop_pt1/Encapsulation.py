class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("ACC123", 5000)
account.deposit(2000)
print("Account Balance:", account.get_balance())
