class User():
    def __init__(self,name,email,account_balance):
        self.name=name
        self.email=email
        self.account_balance =account_balance
    def make_deposit(self,amount):
        self.account_balance+=amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self
    def display_user_balance(self):
        print('user = ',self.name,'and his balance is =',self.account_balance) 
        return self   

yousef = User('yousef atta','yo@atta.com',200)
yousef.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance()


mahmoud = User('mahmoud','mahmoud@gmail.com',400)
mahmoud.make_deposit(200).make_deposit(300).make_withdrawal(200).make_withdrawal(300).display_user_balance()

saleh = User('saleh','saleh@gmail.com',300)
saleh.make_deposit(400).make_withdrawal(400).make_withdrawal(500).make_withdrawal(600).display_user_balance()