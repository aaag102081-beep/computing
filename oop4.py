class Account():
    def __init__(self,account_number,owner,balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance = self.balance + amount
            print("Deposited",amount)
            print("New Balance",self.balance)
    
    def withdraw(self,amount):
        if amount>0 and amount < self.balance:
            self.balance = self.balance-amount
            print("Withdrew:",amount)
            print("New Balance",self.balance)
        else:
            print("Invalid Balance")

class SavingAccount(Account):
    def __init__(self, account_number, owner, balance=0,interest_rate = 0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        return f"Interest on money {self.balance}: {interest}"



sac = SavingAccount(342,"Anaya",560,0.1)
sac.deposit(200)
print(sac.calculate_interest())