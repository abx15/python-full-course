class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance


# Savings Account (Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=5):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest added: {interest}")


# Current Account (Inheritance + Polymorphism)
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount): 
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            if amount <= self.get_balance():
                super().withdraw(amount)  
            else:
                diff = amount - self.get_balance()
                super().withdraw(self.get_balance()) 
                print(f"Overdraft used: {diff}. Balance is negative: {new_balance}")
        else:
            print("Withdrawal exceeds overdraft limit")


# ---------- USAGE ----------

# Savings Account
s_acc = SavingsAccount(201, 1000, 10)
s_acc.add_interest()    
print("Final Balance in Savings:", s_acc.get_balance())

print("----")

# Current Account
c_acc = CurrentAccount(301, 500, 2000)
c_acc.withdraw(800)     
print("Balance after withdrawal:", c_acc.get_balance())
c_acc.withdraw(3000)    
