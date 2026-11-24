
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited successfully")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn successfully")
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance")


# Get details from user
acc_no = input("Enter account number: ")
name = input("Enter name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Create object
a = BankAccount(acc_no, name, acc_type, balance)

# Deposit amount
d = float(input("Enter amount to deposit: "))
a.deposit(d)

# Withdraw amount
w = float(input("Enter amount to withdraw: "))
a.withdraw(w)

