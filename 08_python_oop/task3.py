# create a customer class and a BankAccount Class Each customer can have one bank account implement methods to deposit and withdraw money


class BankAccount:
    def __init__(self, acc_number, balance=0):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, acc_number, balance=0):
        self.name = name
        self.account = BankAccount(acc_number, balance)  

    def show_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.account.acc_number}")
        print(f"Balance: ₹{self.account.get_balance()}")



customer1 = Customer("Arun Kumar", "ACC101", 5000)

customer1.show_details()  # Customer details
customer1.account.deposit(2000)  # Deposit
customer1.account.withdraw(3000)  # Withdraw
customer1.account.withdraw(6000)  # Withdraw (insufficient balance)
