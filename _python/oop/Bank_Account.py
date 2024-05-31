class Bank_Account():
    def __init__(self,balance,interest_rate,fees):
        self.balance = 0
        self.interest_rate = 0.01
        self.fees=fees
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        self.balance -= amount
        if self.fees < 5:
            print('Insufficient funds: Charging a $5 fee" and deduct $5')
        return self
    def display_account_info(self):
        print('Balance : ',self.balance)
        return self        
    def yeild_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

fst_account = Bank_Account(200,0.2,3)
fst_account.deposit(100).deposit(50).deposit(30).withdraw(70).yeild_interest().display_account_info()

scnd_account=Bank_Account(80,0.9,5)
scnd_account.deposit(100).deposit(80).withdraw(40).withdraw(50).withdraw(60).withdraw(70).yeild_interest().display_account_info()

        
        