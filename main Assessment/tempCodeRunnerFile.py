class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited successfully!")
    
    def withdrew(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Account holder:",self.name)
        print("CURRENT BALANCE:",self.balance)


# create account

name = input("Enter account holder name:")
account = BankAccount(name)

while True:
    print("\n ------BANK MENU------")
    print("\n 1.Deposit")
    print("\n 2.Withdraw")
    print("\n 3.Check Balance ")
    print("\n 4.Exit")

choice = input("Enter choicw between 1 to 4:")

if choice == "1":
    amount = int(input("Enetr amount to deposit:"))
    account.deposit(amount)
elif choice == "2":
    amount = int(input("Enter amount to withdraw:"))
    account.withdrew(amount)
elif choice == "3":
    account.check_balance()
elif choice == "4":
    print("Thank you for using Bank management system!")
     break
else:
    print("Inavlid choice .Please try again!")