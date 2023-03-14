class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance is {self.balance}")

    def get_balance(self):
        print(f"Current balance is {self.balance}")

    def __str__(self):
        return f"Account of {self.name} with balance {self.balance}"

# create an account
account = Account("ness gicho", 1000)

# make a deposit
account.deposit(500)

# make a withdrawal
account.withdraw(200)


account.get_balance()

print(account)