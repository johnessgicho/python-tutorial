# Bank System Program

class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. Your new balance is: ${}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal successful. Your new balance is: ${}".format(self.balance))

    def display_balance(self):
        print("Your current balance is: ${}".format(self.balance))

# User Input
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
balance = float(input("Enter your balance: "))

# Creating Bank Account
account = Bank(name, account_number, balance)

# Options for User
print("\nWelcome {}!".format(name))
print("What would you like to do today?")
print("1. Deposit")
print("2. Withdraw")
print("3. Display balance")

# User Input for Options
option = int(input("Enter the number of the option you would like to choose: "))

# Running User's Option
if option == 1:
    amount = float(input("Enter the amount you would like to deposit: $"))
    account.deposit(amount)
elif option == 2:
    amount = float(input("Enter the amount you would like to withdraw: $"))
    account.withdraw(amount)
elif option == 3:
    account.display_balance()
else:
    print("Invalid option selected.")