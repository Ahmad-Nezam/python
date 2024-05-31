class User():
    def __init__(self,name,email,account_balance):
        self.name=name
        self.email=email
        self.account_balance =account_balance
    def make_deposit(self,amount):
        self.account_balance+=amount
    def make_withdrawal(self,amount):
        self.account_balance-=amount
    def display_user_balance(self):
        print('user = ',self.name,'and his balance is =',self.account_balance) 

yousef = User('yousef atta','yo@atta.com',200)
yousef.make_deposit(100)
yousef.make_deposit(200)
yousef.make_deposit(300)
yousef.make_withdrawal(100)
yousef.display_user_balance()           

mahmoud = User('mahmoud','mahmoud@gmail.com',400)
mahmoud.make_deposit(200)
mahmoud.make_deposit(300)
mahmoud.make_withdrawal(200)
mahmoud.make_withdrawal(300)
mahmoud.display_user_balance()

saleh = User('saleh','saleh@gmail.com',300)
saleh.make_deposit(400)
saleh.make_withdrawal(400)
saleh.make_withdrawal(500)
saleh.make_withdrawal(600)
saleh.display_user_balance()