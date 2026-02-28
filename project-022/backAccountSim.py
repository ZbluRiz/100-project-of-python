#define the class for bank account simulator
class bankAcc:
    def __init__(self,account_holder,initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    #deposit a money
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount 
            print(f"Deposited ${amount}. New balance ${self.balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdraw ${amount}. New balance ${self.balance}")
        else:
            print("invalid withdrawal amount or insufficient funds.")
    
    def show_details(self):
        print("\n-Account Details-")
        print(f"Account holder : {self.account_holder}")
        print(f"Account balance : {self.balance}")


accounts = {}

def createAccount():
    name = input("Enter account holder's name: ")
    initial_deposit = float(input("Enter intial deposit amount: "))
    account = bankAcc(name,initial_deposit)
    accounts[name] = account
    print("account created succesfully")

def accessAccount():
    name = input("Enter your name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n-Account Menu-")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show details")
            print("4. Exit")

            choice = input("Enter your choice(1-4) : ")
        
            if choice == '1':
                amount = float(input("Enter your deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter your withdraw amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_details()
            elif choice == '4':
                break
            else:
                print("invalid choice. Please select a valid option")
    else:
        print("You don't have an account")


#main menu

while True:
    print("\n- Bank account simulator-")
    print("1. Create an account")
    print("2. Access account")
    print("3. Exit")
    
    choice = input("enter your choice (1-3): ")
    
    print(accounts)
    
    if choice == '1':
        createAccount()
    elif choice == '2':
        accessAccount()
    elif choice == '3':
        break
    else:
        print("please input a valid choice")
            
        
        