class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Create account
name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n------ BANK MENU ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice between 1 to 4: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again!")
