class Bank_acc:
    def __init__(self, account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance +=amount
        print(f"Total Balance is {self.balance}")

    def withdraw (self,amount):
        if (self.balance>amount):
            self.balance -=amount
            print(f"You have withdrawl {amount}, \nYour Balance is {self.balance}")
        else:
            print("Insufficent balance")

    def view_balance (self):
        print(f"Your Account balance is{self.balance}")

o1 = Bank_acc(1254,"Krishna",584214865)
o1.deposit(1)
o1.view_balance()
o1.withdraw(100)